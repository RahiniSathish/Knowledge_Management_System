import requests

def test_query():
    data = {
        "knowledge_name": "AI-Research",
        "question": "AI concept 10"
    }

    response = requests.post("http://127.0.0.1:8000/query", json=data)
    print(response.json())

if __name__ == "__main__":
    test_query()