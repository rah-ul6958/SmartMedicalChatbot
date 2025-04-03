
# Smart Medical Chatbot Directory Structure

smart_medical_chatbot/
├── main.py              # 🚀 Entry point (Runs FastAPI server & Gradio UI)
├── chatbot.py           # Core chatbot logic (Groq API, Speech & Text Handling)
├── config.py            # Configuration settings (Loads .env)

├── utils/               # Utilities (Audio, Image, Speech Processing)
│   ├── audio.py         # Recording, Transcription, TTS ✅
│   ├── image.py         # Image processing ✅
│   ├── stt.py           # Speech-to-text ✅
│   ├── tts.py           # Text-to-speech ✅

├── services/            # Handles external API interactions
│   ├── groq_client.py   # Groq API handling (Vision + Text AI)
│   ├── tts_service.py   # ElevenLabs TTS API calls

├── interfaces/          # UI & User interaction
│   ├── gradio_interface.py   # Gradio-based Chatbot UI


# Smart Medical Chatbot (with Vision and Voice)

This project is a smart medical chatbot that uses voice and vision input to generate a doctor-like response. Users can record their voice (via microphone) and optionally upload an image. The system transcribes the audio, analyzes the image, and then responds with both text and synthesized speech.

## Features
- **Voice Input:** Record audio via microphone.
- **Image Input:** Upload images for analysis.
- **Speech-to-Text:** Transcribe recorded audio.
- **Image Analysis:** Analyze images using a multimodal API (Groq).
- **Text-to-Speech:** Generate audio responses using ElevenLabs TTS.
- **Gradio UI:** User-friendly interface for interaction.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run main.py
