from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3"
)


def build_retriever(vectorstore):

    return vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )