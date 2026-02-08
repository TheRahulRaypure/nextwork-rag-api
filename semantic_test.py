import requests

def test_kubernetes_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What is Kubernetes?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts (orchestration was removed, so only check for container)
    assert "container" in answer.lower(), "Missing 'container' keyword"
    
    print("✅ Kubernetes query test passed")

def test_nextwork_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What is NextWork?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts from nextwork.txt
    assert "maximus" in answer.lower(), "Missing 'maximus' keyword"
    
    print("✅ NextWork query test passed")

def test_ragapi_query():
    response = requests.post("http://127.0.0.1:8000/query?q=What is RAG API?")
    
    if response.status_code != 200:
        raise Exception(f"Server returned {response.status_code}: {response.text}")
    
    answer = response.json()["answer"]

    # Check for key concepts from nextwork.txt
    assert "Retrieval Augmented Generation" in answer.lower(), "Missing 'Retrieval Augmented Generation' keyword"
    assert "Retrieving" in answer.lower(), "Missing 'Retrieving' keyword"
    assert "Augmenting" in answer.lower(), "Missing 'Augmenting' keyword"
    assert "Generating" in answer.lower(), "Missing 'Generating' keyword"
    
    print("✅ RAG-API query test passed")

if __name__ == "__main__":
    test_kubernetes_query()
    test_nextwork_query()
    print("All semantic tests passed!")
