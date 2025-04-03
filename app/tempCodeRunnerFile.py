import sys
import os
import logging
from app.chatbot import chatbot_loop


# Ensure the project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Optional: Add Gradio UI if implemented
try:
    from app.interfaces.gradio_interface import launch_gradio
    HAS_GRADIO = True
except ImportError:
    HAS_GRADIO = False

# Configure logging
logging.basicConfig(level=logging.INFO)

# Enable/Disable TTS via Environment Variable
ENABLE_TTS = os.getenv("ENABLE_TTS", "True").lower() == "true"

def main():
    """
    Entry point for Smart Medical Chatbot. Runs either CLI chatbot or Gradio UI.
    """
    logging.info("🚀 Starting Smart Medical Chatbot...")
    
    if not ENABLE_TTS:
        logging.info("🔇 TTS is DISABLED. Responses will be displayed as text.")

    if HAS_GRADIO:
        logging.info("🖥️ Launching Gradio UI...")
        launch_gradio()
    else:
        logging.info("🗣️ Running chatbot in CLI mode...")
        chatbot_loop()

if __name__ == "__main__":
    main()
