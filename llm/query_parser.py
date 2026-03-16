from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from app.config import config
from app.logger import get_logger

logger = get_logger()

llm = ChatGroq(
    groq_api_key=config.GROQ_API_KEY,
    model_name="llama3-70b-8192",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
"""
Convert the user query into a short visual search phrase.

Query: {query}

Return only the refined search phrase.
"""
)


def parse_query(user_query):

    try:

        logger.info(f"Original query: {user_query}")

        messages = prompt.format_messages(query=user_query)

        response = llm.invoke(messages)

        refined = response.content.strip()

        logger.info(f"Refined query: {refined}")

        return refined

    except Exception as e:

        logger.error(f"LLM failed: {e}")

        return user_query
