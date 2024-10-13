import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


image_path = "images/bikinizilla.png"

image_upload = genai.upload_file(path=image_path, display_name="Bikini Zilla")

print(f"Uploaded file '{image_upload.display_name}' as: {image_upload.uri}")

file = genai.get_file(name=image_upload.name)
print(f"Retrieved file '{file.display_name}' from: {file.uri}")