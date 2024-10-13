import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
]


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=SAFETY_SETTINGS,
    system_instruction="You are Sherlock Holmes. You will help me solve my questions and mysteries about anything and everything, using your superior analytical skills and reasoning power, all while staying in character as Sherlock Holmes.",
)

history = []

chat_session = model.start_chat(history=history)


if __name__ == "__main__":
    image_path = input("Please provide the path to the image: ")
    image_upload = genai.upload_file(path=image_path, display_name="User Image")

    text_query = input("Please ask a question to go with your image upload: ")

    full_query = [image_upload, text_query]
    response = chat_session.send_message(full_query)

    print(response.text)