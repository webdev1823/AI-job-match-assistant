import os

from google import genai
from google.genai import types

# Free-tier friendly Gemini model. Change it without editing code: set GEMINI_MODEL in the terminal.
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")


def ask_llm(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Set it in the same terminal window, then restart the app.")
    client = genai.Client(api_key=api_key)
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful career assistant. Be concise and honest.",
            max_output_tokens=2000,
        ),
    )
    return resp.text or "The model returned an empty response. Please try again."
