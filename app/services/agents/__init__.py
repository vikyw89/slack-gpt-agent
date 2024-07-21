import os
from langgraph.prebuilt.chat_agent_executor import create_tool_calling_executor
from langchain_openai.chat_models import ChatOpenAI
from app.services.agents.tools.calculator_tool import sum_two_numbers_tool


model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")


runnable = create_tool_calling_executor(model=model, tools=[sum_two_numbers_tool])
