from gradio import Blocks, Markdown, Textbox, Button
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
        result = f"Error: {e}"

    return result


with Blocks() as i_face:
    Markdown(
        """
        # RefineMyWords
        Start typing sentences you'd like to refine.
        """)

    inp = Textbox(label="Input your original text:")
    submit_btn = Button("Refine My Words!")
    out = Textbox(label="Refined version:")

    # Link the button to the function
    submit_btn.click(refine_word, inputs=inp, outputs=out)

if __name__ == "__main__":
    i_face.launch(share=True)
