from fastapi import FastAPI, HTTPException
from database import setup_database
from models import KnowledgeBase, KnowledgeUpdate, DocumentBase, QueryRequest
import crud

app = FastAPI()

# -------------------- Root Endpoint --------------------
@app.get("/")
def home():
    return {"message": "Knowledge Management API is running!"}

# -------------------- Knowledge Endpoints --------------------
@app.post("/knowledge/create")
def create_knowledge(knowledge: KnowledgeBase):
    knowledge_id = crud.create_knowledge(knowledge.name, knowledge.etc)
    return {"status": "success", "knowledge_id": knowledge_id}

@app.put("/knowledge/{knowledge_id}")
def update_knowledge(knowledge_id: int, knowledge: KnowledgeUpdate):
    crud.update_knowledge(knowledge_id, knowledge.etc)
    return {"status": "updated"}

@app.delete("/knowledge/{knowledge_id}")
def delete_knowledge(knowledge_id: int):
    crud.delete_knowledge(knowledge_id)
    return {"status": "deleted"}

# -------------------- Document Endpoints --------------------
@app.post("/document/add")
def add_document(document: DocumentBase):
    crud.add_document(document.knowledge_id, document.filename, document.content)
    return {"status": "success"}

# -------------------- Query Endpoint --------------------
@app.post("/query")
def query_documents(query: QueryRequest):
    result = crud.query_documents(query.knowledge_name, query.question)
    return {"answer": result}

# -------------------- Run Setup --------------------
if __name__ == "__main__":
    setup_database()