from loaders.pdf_loader import PDFLoader
from services.vector_db import VectorDB

pdf_path = r"C:\Users\ASUS\25\data\hema resum24 july (1).pdf"

docs = PDFLoader.load_pdf(pdf_path)

db = VectorDB.create(docs)

print("Database Created Successfully")