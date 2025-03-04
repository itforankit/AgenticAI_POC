from src.langgraphagenticai.state.state import State

class ToolNode:
    def __init__(self, tools):
        """
        Initialize the ToolNode with a dictionary of tool functions.
        :param tools: A dictionary where keys are tool names and values are functions.
        """
        self.tools = tools  # Store tools dictionary

    def process(self, state: State) -> State:
        user_query = state.get("query", "").strip()
        print("ToolNode received query:", user_query)  # Debug print

        if self.tools and user_query:
            for tool_name, tool_function in self.tools.items():
                if callable(tool_function):
                    response = tool_function(user_query)
                    # Update state with each tool's response
                    state[f"tool_response_{tool_name}"] = response
                    print(f"Tool {tool_name} responded with: {response}")  # Debug
        return state
