import os
import logging
import requests
from app.config import settings

# ElevenLabs API Configuration
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default Voice ID
ELEVENLABS_API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

# Enable or Disable TTS
ENABLE_TTS = True  # Set to False to disable ElevenLabs API calls

def text_to_speech(text: str, output_path: str = "output_audio.mp3") -> str:
    """
    Converts text into speech using ElevenLabs API and saves it as an MP3 file.

    :param text: The text to be converted into speech.
    :param output_path: Path to save the generated speech file.
    :return: The file path of the saved speech audio.
    """
    if not ENABLE_TTS:
        logging.info(f"🗣️ [TTS DISABLED] AI Response: {text}")
        return ""  # Skip TTS processing

    headers = {
        "Content-Type": "application/json",
        "xi-api-key": settings.ELEVENLABS_API_KEY
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2",  # Faster model for low latency
        "voice_settings": {"stability": 0.6, "similarity_boost": 0.7}
    }

    try:
        response = requests.post(ELEVENLABS_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            with open(output_path, "wb") as audio_file:
                audio_file.write(response.content)
            logging.info(f"TTS audio saved at: {output_path}")
            return output_path
        else:
            logging.error(f"ElevenLabs API Error: {response.json()}")
    except Exception as e:
        logging.error(f"Error in TTS conversion: {e}")
    
    return ""
