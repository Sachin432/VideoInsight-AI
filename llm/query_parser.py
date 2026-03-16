from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from app.config import config
from app.logger import get_logger

logger = get_logger()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=config.GROQ_API_KEY,
    model_name="llama3-70b-8192",
    temperature=0
)

# Prompt template
prompt_template = ChatPromptTemplate.from_template(
"""
You are an AI assistant helping a video search system.

Convert the user's natural language query into a short semantic search phrase
that can be used for video frame retrieval.

Rules:
- Keep it concise
- Remove unnecessary words
- Focus on visual objects, people, or actions
- Return only the refined phrase

User Query:
{query}
"""
)

def parse_query(user_query: str) -> str:
    """
    Convert natural language query into optimized semantic search query
    """

    try:

        logger.info(f"Original query: {user_query}")

        prompt = prompt_template.format_messages(query=user_query)

        response = llm.invoke(prompt)

        refined_query = response.content.strip()

        logger.info(f"Refined query: {refined_query}")

        return refined_query

    except Exception as e:

        logger.error(f"LLM query parsing failed: {e}")

        # fallback to original query
        return user_query