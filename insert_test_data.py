import crud

def insert_test_data():
    knowledge_id = crud.create_knowledge("AI-Research", "Research papers on AI")

    for i in range(1, 6):
        content = "\n".join([f"Page {j}: Content about AI concept {j}" for j in range(1, 16)])
        crud.add_document(knowledge_id, f"document_{i}.txt", content)

if __name__ == "__main__":
    insert_test_data()