from openai import OpenAI
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.prompt_handler import chat
from services.encode_image import encode_img
from core.config import config

api_key=config.openai_api_key

client = OpenAI(api_key=api_key)

def step_send_nf_openai():
    prompt = chat()
    response = client.responses.create(
        model=config.openai_model,
        input=[
            {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {
                    "type": "input_image",
                    "image_url": encode_img(),
                    "detail": "low"
                }
            ]
        }]
    )

    print(response.output_text)


def step_assist_openai():
    prompt = chat()
    response = client.responses.create(
        model=config.openai_model,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {
                        "type": "input_image",
                        "image_url": encode_img(),
                        "detail": "low"
                    }
                ]
            }
        ]
    )

    # Save the model's CSV/plain-text output to a file for download/opening
    csv_output_text = response.output_text
    csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(csv_output_text)
    print(f"CSV salvo em: {csv_path}")

def download_file_openai():
    csv_data = client.files.content("file-WpzskShUtfzyqoJJrQyGWe")
    
    with open("mydata.csv", "wb") as f:  # Note: use "wb" para binary mode
        f.write(csv_data.read())
    
    print("File downloaded successfully")

if __name__ == "__main__":
    download_file_openai()