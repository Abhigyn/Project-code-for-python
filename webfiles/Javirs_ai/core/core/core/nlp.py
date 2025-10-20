import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ai_response(prompt):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return res.choices[0].message.content.strip()
