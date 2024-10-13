import gradio as gr
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from generate_image import generate_image, download_and_save_image

load_dotenv()


short_story_prompt = ChatPromptTemplate.from_template(
    """
    Please give me a short story where the main character is a(n) {word} and make it very bizarre. The story should have two to three paragraphs and proper formatting."
    Story:
    """
)

image_description_prompt = ChatPromptTemplate.from_template(
    """
    Please take the following story and describe the image that would go with it (Return a prompt for an image generator). Keep in mind the main character of this story is a(n) {word}.
    Story: {story}
    Your prompt for the image generator:
    """
)

llm = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

story_chain = short_story_prompt | llm | output_parser
image_description_chain = image_description_prompt | llm | output_parser


def run_chain(word: str):
    story = story_chain.invoke({"word": word})
    print("story:", story, end="\n\n")

    image_description = image_description_chain.invoke(
        {
            "word": word,
            "story": story,
        }
    )
    print("image description:", image_description)

    image_url = generate_image(image_description)
    image_file_path = download_and_save_image(image_url)

    return story, image_file_path


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("# Silly-o-Matic Story Generator Thing...")
        with gr.Column():
            with gr.Row():
                word_input = gr.Textbox(
                    label="Who or what is the main character of your story?",
                    placeholder="e.g. 'a talking banana'",
                    autofocus=True,
                    max_length=40,
                )
            with gr.Row():
                submit_button = gr.Button(
                    value="🤪 Generate a silly story for me! ٩(^ᗜ^ )و ( ≧ᗜ≦)´-( °ヮ° ) ?",
                    variant="primary",
                    size="lg",
                )
            with gr.Row():
                story_output = gr.Textbox(
                    label="Generated Story",
                    lines=20,
                    max_lines=40,
                    show_copy_button=True,
                )
                image_output = gr.Image(
                    label="Generated Image",
                    show_download_button=True,
                    show_share_button=True,
                    show_fullscreen_button=True,
                )

        submit_button.click(
            run_chain, inputs=word_input, outputs=[story_output, image_output]
        )

    demo.launch()