import os
import logging
import requests
from app.config import settings

# ElevenLabs API Configuration
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default Voice ID
ELEVENLABS_API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"

# Enable/Disable TTS via Environment Variable
ENABLE_TTS = os.getenv("ENABLE_TTS", "True").lower() == "true"

# Define a dummy silent audio file
DUMMY_AUDIO_PATH = "silent_audio.mp3"

def generate_dummy_audio():
    """Generates a silent 1-second MP3 file (if not already created)."""
    if not os.path.exists(DUMMY_AUDIO_PATH):
        with open(DUMMY_AUDIO_PATH, "wb") as f:
            f.write(b"\x00" * 1024)  # Creates a silent audio file
        logging.info("✅ Generated a silent dummy audio file.")

def text_to_speech(text: str, output_path: str = "output_audio.mp3") -> str:
    """
    Converts text into speech using ElevenLabs API and saves it as an MP3 file.
    Returns a dummy silent audio file when TTS is disabled.
    """
    if not ENABLE_TTS:
        logging.info("🔇 TTS is DISABLED. Returning dummy silent audio.")
        generate_dummy_audio()  # Ensure dummy file exists
        return DUMMY_AUDIO_PATH  # Return the dummy silent file

    headers = {
        "Content-Type": "application/json",
        "xi-api-key": settings.ELEVENLABS_API_KEY
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {"stability": 0.6, "similarity_boost": 0.7}
    }

    try:
        response = requests.post(ELEVENLABS_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            with open(output_path, "wb") as audio_file:
                audio_file.write(response.content)
            logging.info(f"🎙️ TTS audio saved at: {output_path}")
            return output_path
        else:
            logging.error(f"❌ ElevenLabs API Error: {response.json()}")
    except Exception as e:
        logging.error(f"❌ Error in TTS conversion: {e}")
    
    # If TTS API call fails, return dummy silent audio
    generate_dummy_audio()
    return DUMMY_AUDIO_PATH
