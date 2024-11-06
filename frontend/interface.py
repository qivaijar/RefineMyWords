from gradio import Blocks, Markdown, Textbox, Button, Row, Column
import requests
from dotenv import load_dotenv
import os

# Loading environment parameters
load_dotenv()
api_url = os.getenv("API_URL")


def refine_word(input_text: str) -> str:
    try:
        refine_url = api_url + '/refine'
        response = requests.post(
            refine_url,  # Replace with your FastAPI endpoint
            json={"sentence": input_text}
        )
        # Check if the request was successful
        response.raise_for_status()
        result = response.json().get("refined_sentence", "Error: No refined text returned.")
    except requests.exceptions.RequestException as e:
        result = f"Cannot connect to the API service"

    return result


with Blocks() as i_face:
    Markdown(
        """
        # RefineMyWords
        Start typing sentences you'd like to refine.
        """)
    with Row():
        with Column(scale=1):
            input_text = Textbox(label="Input your original text:", lines=10)
        with Column(scale=0):
            submit_button = Button(value="Refine My Words!", variant='primary')
        with Column(scale=1):
            output_text = Textbox(label="Refined version:", lines=10)

    # Refine the text!
    submit_button.click(refine_word, inputs=input_text, outputs=output_text)

if __name__ == "__main__":
    i_face.launch(share=True)
