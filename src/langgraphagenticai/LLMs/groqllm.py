import os
import streamlit as st
from langchain_groq import ChatGroq
#from src.langgraphagenticai.tools.multitools import combinedtools

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input['GROQ_API_KEY']
            selected_groq_model=self.user_controls_input['selected_groq_model']
            if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                st.error("Please Enter the Groq API KEY")

            llm = ChatGroq(api_key =groq_api_key, model=selected_groq_model)
          #  ll,_with_tools = llm.bind_tools(tools=Combinedtools())

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        return llm
    
"""  
def get_llm_model_with_tools(self):
    try:
        groq_api_key=self.user_controls_input['GROQ_API_KEY']
        selected_groq_model=self.user_controls_input['selected_groq_model']
        if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
            st.error("Please Enter the Groq API KEY")

        llm = ChatGroq(api_key =groq_api_key, model=selected_groq_model)
        tools=combinedtools()
        llm_with_tools = llm.bind_tools(tools=tools)

    except Exception as e:
        raise ValueError(f"Error Occurred with Exception : {e}")
    return llm_with_tools 
"""