import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_text(text: str) -> dict:
    """Send a prompt to OpenAI and get a structured JSON response."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a text analyzer. Always respond with valid JSON only. No explanation, no markdown, just raw JSON."
                },
                {
                    "role": "user",
                    "content": f"Analyze this text and return a JSON with these fields: sentiment (positive/negative/neutral), word_count (integer), summary (one sentence).\n\nText: {text}"
                }
            ],
            temperature=0.2  # low = more consistent output
        )

        # Extract the text content from response
        raw = response.choices[0].message.content

        # Parse into Python dict
        result = json.loads(raw)
        return result

    except json.JSONDecodeError:
        print("Error: Model did not return valid JSON")
        return {}
    except Exception as e:
        print(f"API Error: {e}")
        return {}


if __name__ == "__main__":
    sample_text = "I just finished setting up my first AI project. It was challenging but incredibly rewarding."
    
    print("Sending request to OpenAI...\n")
    result = analyze_text(sample_text)
    
    if result:
        print("Response received:")
        print(json.dumps(result, indent=2))