import os
import faiss
import pickle
from utilities.chunking import chunk_data;
from utilities.embeddings import generate_embeddings;
import numpy as np

def load_faiss_index():
    if os.path.exists("faiss_store/index.faiss"):
        index = faiss.read_index("faiss_store/index.faiss")
        with open("faiss_store/chunk_mapping.pkl", "rb") as f:
            chunk_mapping = pickle.load(f)
    else:
        with open("data/careers.txt", "r", encoding="utf-8") as f:
            text = f.read();
            chunks = chunk_data(text, size=100);  # Using a default chunk size of 100 words
            chunk_mapping = [];
            index = faiss.IndexFlatL2(384) ;
            for chunk in chunks:
                emb = generate_embeddings(chunk);
                index.add(np.array([emb]).astype("float32"));
                chunk_mapping.append(chunk);

        os.makedirs("faiss_store", exist_ok=True);
        faiss.write_index(index, "faiss_store/index.faiss");
        with open("faiss_store/chunk_mapping.pkl", "wb") as f:
            pickle.dump(chunk_mapping, f);
    
    return index, chunk_mapping;

def retrieve_chunks(query, index, chunk_mapping, k=3):

    query_vec = generate_embeddings(query);
    
    dim, indices = index.search(np.array([query_vec]).astype("float32"), k);

    return [chunk_mapping[i] for i in indices[0]];