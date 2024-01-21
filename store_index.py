from src.helper import load_csv,download_hugging_face_embeddings
from langchain.vectorstores import FAISS

import os



DB_FAISS_PATH = "Vectorstores/db_faiss"

extracted_data = load_csv("data/")
embeddings = download_hugging_face_embeddings()
db = FAISS.from_documents(extracted_data,embeddings)
db.save_local(DB_FAISS_PATH)


