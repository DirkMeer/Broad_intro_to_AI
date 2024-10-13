import os
import uuid
import requests

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_image(image_description):
    response = CLIENT.images.generate(
        model="dall-e-3",
        prompt=image_description,
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    print(f"Generated image: {image_url}")
    return image_url


def download_and_save_image(url):
    response = requests.get(url)
    image_name = uuid.uuid4()
    image_path = os.path.join("output", f"{image_name}.png")

    with open(image_path, "wb") as file:
        file.write(response.content)

    print(f"Image saved to {image_path}")

    return image_path


if __name__ == "__main__":
    image_description = input("Enter a description of the image you want to generate: ")
    image_url = generate_image(image_description)
    download_and_save_image(image_url)