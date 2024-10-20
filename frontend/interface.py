from gradio import Blocks, Markdown, Textbox

def refine_word(input_text: str) -> str:
    result = input_text
    return result

with Blocks() as i_face:
        Markdown(
        """
        # RefineMyWords
        Start typing sentences you'd like to refine.
        """)

        inp = Textbox(label="Original Text")
        out = Textbox(label="Refined Text")

        inp.change(refine_word, inp, out)

if __name__ == "__main__":
    i_face.launch(share=True)
    
