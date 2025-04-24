"""Define a simple chatbot agent.

This agent returns a predefined response without using an actual LLM.
"""

from typing import Literal

from langgraph.graph import StateGraph

from agent.state import State


async def node_a(state: State) -> State:
    """First node that increments the counter."""
    print(f"Node A: Counter = {state.counter}")
    return State(counter=state.counter + 1)

def node_b(state: State) -> State:
    """Second node that just reports the counter."""
    print(f"Node B: Counter = {state.counter}")
    return state

# Define the conditional edge function
def conditional_edge(state: State) -> Literal["node_a", "__end__"]:
    """Determine if we should loop back to Node A or end."""
    if state.counter < 27:  # This will cause us to loop 26 times (exceeding the default limit of 25)
        print(f"Routing back to Node A (counter = {state.counter})")
        return "node_a"
    else:
        print(f"Ending execution (counter = {state.counter})")
        return "__end__"

# Define a new graph
workflow = StateGraph(State)

# Add the nodes
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)

# Add edges
workflow.add_edge("node_a", "node_b")
workflow.add_conditional_edges("node_b", conditional_edge)

# Set the entry point
workflow.set_entry_point("node_a")
    
# Compile the workflow into an executable graph
graph = workflow.compile()
graph.name = "New Graph"  # This defines the custom name in LangSmith
