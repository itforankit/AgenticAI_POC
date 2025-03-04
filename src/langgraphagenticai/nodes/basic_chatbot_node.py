from src.langgraphagenticai.state.state import State
from langchain.schema import HumanMessage, AIMessage

class BasicChatbotNode:
    """
    Basic chatbot logic implementation.
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}
    
    """ def process(self, state: State) -> State:
        #Processes the input state and generates a chatbot response.
        #return {"messages":self.llm.invoke(state['messages'])}
        if "messages" not in state or not state["messages"]:
            raise ValueError("User query is empty. Please provide a query.")
        
        # Get the first message from state
        first_message = state["messages"][0]
    
        print("🤖 Chatbot Invoked!")  # Debugging print
        # If it's an instance of HumanMessage, extract its content
        user_query = first_message.content.strip() if hasattr(first_message, "content") else ""
        
        if not user_query:
            raise ValueError("User query is empty. Please provide a query.")
        
        # Check if a tool response exists
        #for key in state:
        #    if key.startswith("tool_response_"):
        #        print(f"📌 Using tool response: {state[key]}")
        #        return state  # Exit early if tool response is found

        #print("🧠 Calling LLM for:", user_query)
        #llm_response = self.llm(user_query)  # Ensure LLM is callable
        #state["llm_response"] = llm_response
        #print("✅ LLM Response:", llm_response)
        
        # Build the messages payload. (For example, OpenAI Chat API expects a list of messages.)
        messages = [HumanMessage(content=user_query)]
        print("LLM message payload:", messages)  # Debug statement
        
        # Invoke the LLM
        llm_response = self.llm(messages=messages)
        state["llm_response"] = llm_response

        # Wrap the LLM response in an AIMessage
        assistant_message = AIMessage(content=llm_response)
        state.setdefault("messages", []).append(assistant_message)
        state["llm_response"] = llm_response
        
        # Append the LLM response to state messages (if needed)
        #state.setdefault("messages", []).append({"role": "assistant", "content": llm_response})
        return state """