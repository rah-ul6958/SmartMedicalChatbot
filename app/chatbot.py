import os
import sys
import logging
from app.utils.stt import record_audio, transcribe_audio
from app.config import settings
from app.services.groq_client import get_ai_response
from app.services.tts_service import text_to_speech, ENABLE_TTS

# Ensure the project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Configure logging
logging.basicConfig(level=logging.INFO)

def chatbot_loop():
    """
    Runs the chatbot loop: listens, transcribes, gets AI response, and speaks.
    """
    logging.info("🤖 Smart Medical Chatbot is running! Say 'exit' to stop.")

    if not ENABLE_TTS:
        logging.info("🔇 TTS is DISABLED. AI responses will be text only.")

    while True:
        # 1. Record user speech
        audio_path = record_audio()
        if not audio_path:
            continue  # Retry if recording failed

        # 2. Convert speech to text
        user_input = transcribe_audio(audio_path)
        if not user_input or user_input.lower() == "exit":
            logging.info("👋 Exiting chatbot.")
            break

        # 3. Get AI response
        ai_response = get_ai_response(user_input)
        logging.info(f"🤖 AI: {ai_response}")

        # 4. Convert AI response to speech if enabled
        text_to_speech(ai_response)
