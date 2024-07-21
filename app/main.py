import logging
import os
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from app.services.agents import runnable
from langchain_core.messages import SystemMessage, AIMessageChunk
from app.types.index import SlackEvent
from app.utils import to_langchain_messages


logging.basicConfig(level=logging.DEBUG, filemode="a+", filename="app.log")
app = AsyncApp(
    signing_secret=os.getenv("SLACK_SIGNING_SECRET"),
    token=os.getenv("SLACK_BOT_TOKEN")
)

app_handler = AsyncSlackRequestHandler(app)
BUNDLE_STREAM_CHUNK_SIZE = 10


@app.event("app_mention")
async def handle_app_mentions(body, say, logger):
    logger.info(body)
    event = SlackEvent(**body)

    # extract user id and chat history
    res = await app.client.conversations_history(channel=event.event.channel, limit=5)
    chat_history = res.get("messages")
    parsed_messages = to_langchain_messages(messages=chat_history)

    # construct prompt
    system_prompt = f"""Let's think step by step.
    You are a slack assistant.
    You will receive a list of messages.
    Your bot id is {os.getenv("SLACK_BOT_ID")}"""

    system_message = SystemMessage(content=system_prompt)

    # call LLM
    response_stream = runnable.astream_events(
        input={"messages": [system_message] + parsed_messages}, version="v2"
    )

    slack_response = await say(" ")
    final_message_content = ""

    chunk_count = 0
    async for chunk in response_stream:
        logger.info(chunk)
        event = chunk["event"]
        data = chunk["data"]

        if event == "on_chat_model_stream":
            stream_chunk: AIMessageChunk = data["chunk"]
            final_message_content += str(stream_chunk.content)
            chunk_count += 1

            if chunk_count % 10 == 0:
                await app.client.chat_update(
                    channel=slack_response.get("channel"),
                    ts=slack_response.get("ts"),
                    text=final_message_content,
                )

    # update final message
    await app.client.chat_update(
        channel=slack_response.get("channel"),
        ts=slack_response.get("ts"),
        text=final_message_content,
    )


@app.event("message")
async def handle_message(body, say, logger):
    logger.info(body)
    pass


from fastapi import FastAPI, Request

api = FastAPI()


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@api.get("/slack/install")
async def install(req: Request):
    return await app_handler.handle(req)


@api.get("/slack/oauth_redirect")
async def oauth_redirect(req: Request):
    return await app_handler.handle(req)
