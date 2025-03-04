from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[list, add_messages]

def tools_condition(state: State) -> bool:
    """
    A simple condition that checks whether to run tools.
    For example, it looks for a flag 'use_tool' in the state.
    """
    return state.get("use_tool", False)