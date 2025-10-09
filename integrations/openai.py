from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Voce me escuta? se sim quantos dolares isto vai me custar?."
)

print(response.output_text)
