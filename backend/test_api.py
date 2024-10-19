from fastapi.testclient import TestClient
from .main import app


# Create test client object
client = TestClient(app)


def test_refine_sentence():
    # Test case for a valid sentence
    response = client.post("/refine",
                           json={"sentence": "yesterday i go to the market"})
    assert response.status_code == 200
    assert response.json() == {
        "refined_sentence": "Yesterday I went to the market."}
