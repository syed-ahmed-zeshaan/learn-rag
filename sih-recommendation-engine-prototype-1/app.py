import streamlit as st
from utilities.chunking import chunk_data
from utilities.completion import get_gemini_response
from utilities.embeddings import generate_embeddings
from utilities.prompt import generate_prompt
from utilities.retrieval import load_faiss_index, retrieve_chunks

st.title("Career Recommendation Engine Prototype 1 Team Orvia");
st.write("Enter your query below to get career recommendations.");

query=st.text_input("Enter your query here:");

if query:
    index, chunk_mapping = load_faiss_index()
    top_chunks = retrieve_chunks(query, index, chunk_mapping)
    prompt = generate_prompt(top_chunks, query)
    response = get_gemini_response(prompt)
    
    st.subheader("Response:");
    st.write(response);

    with st.expander("Top Retrieved Chunks"):
        for i, chunk in enumerate(top_chunks):
            st.markdown(f"**Chunk {i+1}:** {chunk}")