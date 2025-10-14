from openai import OpenAI
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.prompt_handler import chat
from services.encode_image import encode_img
from core.config import config

api_key=config.openai_api_key

client = OpenAI(api_key=api_key)
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
