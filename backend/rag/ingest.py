import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("startup_knowledge")

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "A startup should solve a real customer problem.",
    "Revenue models include subscription, marketplace and SaaS.",
    "Startups raise funds through angel investors and venture capital.",
    "Social media marketing is important for startup growth."
]

embeddings = model.encode(documents).tolist()

for i, doc in enumerate(documents):
    collection.add(
        ids=[str(i)],
        documents=[doc],
        embeddings=[embeddings[i]]
    )

print("Knowledge Base Created Successfully")    