# TO MOCK LLM FLAG 

import os
from fastapi import FastAPI
import chromadb

# Mock LLM mode for CI testing
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "0") == "1"

if not USE_MOCK_LLM:
    import ollama

app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    if USE_MOCK_LLM:
        # In mock mode, return the retrieved context directly
        return {"answer": context}

    # In production mode, use Ollama
    answer = ollama.generate(
        model="tinyllama",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}




######################################################################################################

# TO TEST WITHOUT DOCKER/K8S
# from fastapi import FastAPI
# import chromadb
# import ollama
# import os

# app = FastAPI()
# chroma = chromadb.PersistentClient(path="./db")
# collection = chroma.get_or_create_collection("docs")
# # Use environment variable for Ollama host, default to localhost for local development
# ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
# ollama_client = ollama.Client(host=ollama_host)

# @app.post("/query")
# def query(q: str):
#     results = collection.query(query_texts=[q], n_results=1)
#     context = results["documents"][0][0] if results["documents"] else ""

#     answer = ollama_client.generate(
#         model="tinyllama",    
#         prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
#     )
    
#     return {"answer": answer["response"]}



######################################################################################################

# FOR DOCKER/K8S VERSION
# from fastapi import FastAPI
# import chromadb
# import ollama

# app = FastAPI()
# chroma = chromadb.PersistentClient(path="./db")
# collection = chroma.get_or_create_collection("docs")
# ollama_client = ollama.Client(host="http://host.docker.internal:11434")


# @app.post("/query")
# def query(q: str):
#     results = collection.query(query_texts=[q], n_results=1)
#     context = results["documents"][0][0] if results["documents"] else ""

#     answer = ollama_client.generate(
#         model="tinyllama",
#         prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
#     )


#     return {"answer": answer["response"]}



