import sys
import os
import logging

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.chatbot import chatbot_loop

# Optional: Add Gradio UI if implemented
try:
    from app.interfaces.gradio_interface import launch_gradio
    HAS_GRADIO = True
except ImportError:
    HAS_GRADIO = False

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    """
    Entry point for Smart Medical Chatbot. Runs either the CLI chatbot or Gradio UI.
    """
    logging.info("🚀 Starting Smart Medical Chatbot...")
    
    if HAS_GRADIO:
        logging.info("🖥️ Launching Gradio UI...")
        launch_gradio()
    else:
        logging.info("🗣️ Running chatbot in CLI mode...")
        chatbot_loop()

if __name__ == "__main__":
    main()
