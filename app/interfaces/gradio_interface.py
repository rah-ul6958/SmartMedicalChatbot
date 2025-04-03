# app/interfaces/gradio_interface.py
import gradio as gr
import logging
from app.services.groq_client import get_ai_response
from app.services.tts_service import text_to_speech
from app.utils.stt import transcribe_audio

# Configure logging
logging.basicConfig(level=logging.INFO)

def chatbot_interaction(audio_file=None, text_input="", image_file=None):
    """
    Handles chatbot interaction via text, audio, or image input.
    
    :param audio_file: Optional audio file for speech input.
    :param text_input: Optional text input.
    :param image_file: Optional image file for image recognition.
    :return: AI response (text) and generated speech file.
    """
    # Prefer audio if provided; otherwise, use text input.
    if audio_file:
        logging.info("🎤 Processing audio input...")
        user_input = transcribe_audio(audio_file)
    elif text_input:
        user_input = text_input
    else:
        return "Please provide text or audio input.", None

    logging.info(f"📝 User Input: {user_input}")
    
    # Get AI response, passing the image file path if provided.
    ai_response = get_ai_response(user_input, image_path=image_file)
    logging.info(f"🤖 AI Response: {ai_response}")
    
    # Convert AI response to speech
    speech_file = text_to_speech(ai_response)
    
    return ai_response, speech_file

def launch_gradio():
    """
    Launches the Gradio UI for the Smart Medical Chatbot.
    """
    with gr.Blocks() as demo:
        gr.Markdown("# 🤖 Smart Medical Chatbot")
        gr.Markdown("Provide text, audio, or an image to interact with the chatbot.")

        with gr.Row():
            text_input = gr.Textbox(label="Type your query here:")
            audio_input = gr.Audio(type="filepath", label="Or speak your query:")
            image_input = gr.Image(type="filepath", label="Or upload an image:")

        submit_button = gr.Button("Submit")
        
        with gr.Row():
            text_output = gr.Textbox(label="Chatbot Response", interactive=False)
            audio_output = gr.Audio(label="Audio Response", interactive=False)
        
        submit_button.click(fn=chatbot_interaction, inputs=[audio_input, text_input, image_input], outputs=[text_output, audio_output])

    demo.launch(share=True)
