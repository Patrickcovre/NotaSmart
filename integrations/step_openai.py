from openai import OpenAI
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.config import config

api_key=config.openai_api_key

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model=config.openai_model,
    input="Oi meu nome e patrick pfv diga bom dia patrick?"
)

print(response.output_text)
