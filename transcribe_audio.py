import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def transcribe_audio(audio_file):
    response = CLIENT.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    
    transcript = response.text
    print(f"Transcription:\n{transcript}")
    return transcript


if __name__ == "__main__":
    audio_file = open("test_audio.mp3", "rb")
    transcribe_audio(audio_file)