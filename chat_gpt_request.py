import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


summarizing_instructions = """
You are a helpful assistant for summarizing information. You will be provided with input and your job is to summarize it in a concise and professional manner. Make sure you keep the important key points intact and provide a clear and easy-to-understand summary of the information that is engaging and easy to read.
"""

with open("text_to_summarize.txt", "r", encoding='utf-8') as file:
    text_to_summarize = file.read()


print("Asking SummaryGPT...")
summary = CLIENT.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": summarizing_instructions},
        {"role": "user", "content": text_to_summarize}
    ]
)

extracted_summary = summary.choices[0].message.content
print(extracted_summary)