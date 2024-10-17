import requests

# Define the API endpoint
# Change this to your deployment URL if needed
url = "http://127.0.0.1:8000/refine/"

# Prompt for the input sentence
input_sentence = input("Please enter the text you want to refine:\n ")

# Prepare the test data
data = {
    "sentence": input_sentence
}

# Send a POST request to the API
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    result = response.json()

    print("\nOriginal Sentence:", result["original"])
    print("Refined Sentence:", result["refined"])
else:
    print("Error:", response.status_code, response.text)
