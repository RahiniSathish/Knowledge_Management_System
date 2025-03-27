from database import get_db_connection
def create_knowledge(name: str, etc: str):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO knowledge (name, etc) VALUES (?, ?)", (name, etc))
        conn.commit()
        return cursor.lastrowid

def update_knowledge(knowledge_id: int, etc: str):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE knowledge SET etc = ? WHERE id = ?", (etc, knowledge_id))
        conn.commit()

def delete_knowledge(knowledge_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM knowledge WHERE id = ?", (knowledge_id,))
        conn.commit()

def add_document(knowledge_id: int, filename: str, content: str):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO document (knowledge_id, filename, content) VALUES (?, ?, ?)",
                       (knowledge_id, filename, content))
        conn.commit()

def query_documents(knowledge_name: str, question: str):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT d.content FROM document d
            JOIN knowledge k ON d.knowledge_id = k.id
            WHERE k.name = ?
        ''', (knowledge_name,))
        
        documents = cursor.fetchall()
        return [doc[0] for doc in documents if question.lower() in doc[0].lower()]
