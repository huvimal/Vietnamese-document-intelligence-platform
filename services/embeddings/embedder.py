from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-m3"
)


def generate_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings.tolist()