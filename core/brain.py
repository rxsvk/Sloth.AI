import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

def think(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are SLOTH AI, an autonomous business assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]
