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
    file = client.files.create(
        file=open("mydata.csv", "rb"),
        purpose='assistants'
    )
    assistant = client.beta.assistants.create(
        instructions=prompt,
        model=config.openai_model,
        tools=[
            {"type": "code_interpreter"},
        ],
        tool_resources={
           "code_interpreter": {
            "file_ids": [file.id]
        }
        },
    )
    print(assistant)


def download_file_openai():
    csv_data = client.files.content("file-8mmuJoy7d1QpotK13uyAcT")
    csv_datas = csv_data.decode('utf-8')

    with open("mydata.csv", "w") as f:
        f.write(csv_datas)

    print("File downloaded successfully")

if __name__ == "__main__":
    download_file_openai()