from openai import OpenAI
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.prompt_handler import chat
from core.config import config

api_key=config.openai_api_key

client = OpenAI(api_key=api_key)
prompt = chat()
response = client.responses.create(
    model=config.openai_model,
    input=prompt
)

print(response.output_text)
