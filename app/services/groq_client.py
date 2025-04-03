import requests
import logging
from app.config import settings

# Groq API Configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {settings.GROQ_API_KEY}"
}

def get_ai_response(prompt: str, image_path: str = None) -> str:
    """
    Sends user input (with optional image) to Groq's AI model and retrieves a response.
    
    :param prompt: User's transcribed text input.
    :param image_path: Optional path to an image file.
    :return: AI-generated response.
    """
    # If an image is provided, encode it and use a nested content structure.
    if image_path:
        from app.utils.image import encode_image_to_base64
        encoded_image = encode_image_to_base64(image_path)
        if encoded_image:
            messages = [{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                ]
            }]
        else:
            logging.error("Failed to encode image; proceeding without image data.")
            messages = [{
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }]
    else:
        messages = [{
            "role": "user",
            "content": [{"type": "text", "text": prompt}]
        }]

    payload = {
        "model": settings.IMAGE_MODEL,  # Model must support vision, e.g., a multimodal model.
        "messages": messages,
        "max_tokens": 150
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            result = response.json()
            # Validate response structure:
            if ("choices" in result and isinstance(result["choices"], list) and 
                len(result["choices"]) > 0 and 
                "message" in result["choices"][0] and 
                "content" in result["choices"][0]["message"]):
                return result["choices"][0]["message"]["content"]
            else:
                logging.error(f"Unexpected API response structure: {result}")
                return "I'm sorry, I couldn't understand the response from the server."
        else:
            logging.error(f"❌ Groq API Error: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"❌ Error communicating with Groq API: {e}")
    
    return "I'm sorry, I couldn't process that."
