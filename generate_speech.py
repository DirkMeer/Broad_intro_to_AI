import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def text_to_speech(text):
    response = CLIENT.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    
    first_chars = text[:20]
    speech_file_path = os.path.join("output", f"{first_chars}.mp3")
    response.stream_to_file(speech_file_path)
    
    print(f"Speech saved to {speech_file_path}")
    return response


if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)