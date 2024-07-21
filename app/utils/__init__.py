from app.types import Message
from langchain_core.messages import HumanMessage, AIMessage


def to_langchain_messages(messages: list[dict]) -> list[HumanMessage | AIMessage]:
    parsed_messages = []
    index = len(messages) - 1
    while index >= 0:
        message = Message(**messages[index])
        parsed_messages.append(
            HumanMessage(content=message.text)
            if message.bot_id
            else AIMessage(content=message.text)
        )
        index -= 1
    return parsed_messages
