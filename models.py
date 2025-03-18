from pydantic import BaseModel
from typing import Optional, List

class KnowledgeBase(BaseModel):
    name: str
    etc: Optional[str] = ""

class KnowledgeUpdate(BaseModel):
    etc: str

class DocumentBase(BaseModel):
    knowledge_id: int
    filename: str
    content: str

class QueryRequest(BaseModel):
    knowledge_name: str
    question: str