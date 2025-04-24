"""Define the state structures for the agent."""

from typing import Annotated

from pydantic import BaseModel, Field

class State(BaseModel):
    """Defines the input state for the agent, representing a narrower interface to the outside world.

    This class is used to define the initial state and structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    for more information.
    """

    counter: Annotated[int, "The current counter value", Field(default=0)]
