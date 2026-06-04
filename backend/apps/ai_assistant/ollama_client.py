import requests
import json
from django.conf import settings

OLLAMA_URL = f"{settings.OLLAMA_HOST}/api/generate"

def ask_llama3(prompt: str, system_prompt: str = None) -> str:
    if system_prompt is None:
        system_prompt = "You are CivicFlow AI, an official government services assistant. Answer accurately and helpfully. Keep responses concise."
    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "system": system_prompt,
        "stream": False,
        "options": {"num_predict": 300, "temperature": 0.3}
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json().get('response', 'Sorry, I could not generate a response.')
    except Exception as e:
        return f"AI service error: {str(e)}"