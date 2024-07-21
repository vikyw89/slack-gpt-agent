from typing import Annotated
from langchain_core.tools import StructuredTool
from pydantic import Field


async def sum_two_numbers(
    a: Annotated[int, Field(description="first number")],
    b: Annotated[int, Field(description="second number")],
) -> str:
    """Sum two numbers."""
    return a + b


sum_two_numbers_tool = StructuredTool.from_function(coroutine=sum_two_numbers)
