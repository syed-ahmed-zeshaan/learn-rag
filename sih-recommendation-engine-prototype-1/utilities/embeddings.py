from sentence_transformers import SentenceTransformer

def generate_embeddings(data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(data)
    return embeddings




