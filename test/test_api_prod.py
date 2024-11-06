import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_url = os.getenv("API_URL")


def test_refine_sentence():
    # Test case for a valid sentence
    refine_url = api_url + '/refine'
    response = requests.post(refine_url,
                             json={"sentence": "yesterday i go to the market"})
    print(response.json())


if __name__ == "__main__":
    test_refine_sentence()
