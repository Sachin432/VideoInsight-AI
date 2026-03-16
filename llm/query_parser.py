from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

prompt = ChatPromptTemplate.from_template(
"""
Convert the user query into a short visual search phrase.

Query: {query}

Return only the refined search phrase.
"""
)

def parse_query(user_query):

    try:

        llm = ChatGroq(
            groq_api_key=st.secrets["GROQ_API_KEY"],
            model_name="llama3-70b-8192",
            temperature=0
        )

        messages = prompt.format_messages(query=user_query)

        response = llm.invoke(messages)

        return response.content.strip()

    except Exception as e:

        print("LLM error:", e)

        return user_query
