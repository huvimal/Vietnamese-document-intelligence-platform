from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template(
    """
    Extract invoice information from the following text.

    Return valid JSON.

    TEXT:
    {text}
    """
)


def extract_invoice(text: str):

    chain = prompt | llm

    result = chain.invoke({"text": text})

    return result.content