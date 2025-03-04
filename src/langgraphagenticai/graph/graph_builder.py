from langgraph.graph import StateGraph, START,END, MessagesState
from langgraph.prebuilt import tools_condition #,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.wikitools import wikipedia_tool, arxiv_tool
from src.langgraphagenticai.nodes.ToolNode import ToolNode
import streamlit as st


class GraphBuilder:

    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def basic_chatbot_build_graph_withtools(self):
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        
        # Ensure START connects to another node
        self.graph_builder.set_entry_point("chatbot")  # This ensures the graph has an entry point
        self.graph_builder.add_edge(START,"chatbot")
              
        combinedtools={
            "wiki":wikipedia_tool, 
            "arxiv":arxiv_tool
        }
        
        tool_node=ToolNode(tools=combinedtools)
        
        self.graph_builder.add_node("tools",tool_node.process)
        self.graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition
        )
        self.graph_builder.add_edge("chatbot",END)
       
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Tools":
            self.basic_chatbot_build_graph_withtools()
        return self.graph_builder.compile()



    

