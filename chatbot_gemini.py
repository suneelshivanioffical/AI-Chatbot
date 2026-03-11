from google import genai
from google.genai import types

def get_gemini_response(api_key, user_prompt, model_name):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model_name,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful AI assistant. Keep answers short."
        )
    )

    return response.text