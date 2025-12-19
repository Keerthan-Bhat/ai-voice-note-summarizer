import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(transcript: str):
    # Hard limit to avoid hanging
    transcript = transcript[:4000]

    prompt = f"""
Summarize the following transcript.

Return the result in JSON with:
- summary (string)
- key_points (array of strings)
- action_items (array of strings)

Transcript:
{transcript}
"""

    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 300
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )
    response.raise_for_status()

    raw = response.json().get("response", "").strip()

    # 🔒 SAFETY CHECK
    if not raw:
        return {
            "summary": "No summary could be generated.",
            "key_points": [],
            "action_items": []
        }

    # 🔎 Extract JSON safely
    start = raw.find("{")
    end = raw.rfind("}") + 1

    if start == -1 or end == 0:
        return {
            "summary": raw[:500],  # fallback: show text
            "key_points": [],
            "action_items": []
        }

    try:
        return json.loads(raw[start:end])
    except json.JSONDecodeError:
        return {
            "summary": raw[:500],
            "key_points": [],
            "action_items": []
        }


