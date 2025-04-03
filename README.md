# Smart Medical Chatbot

```
|──app/
├── main.py             # 🚀 Entry Point (FastAPI & Gradio UI)
├── chatbot.py          # 🤖 Core Logic (Groq API, Speech & Text)
├── config.py           # ⚙️ Configuration (.env Loading)
│
├── utils/              # 🛠️ Utility Modules
│   ├── audio.py        # 🎙️ Audio Handling (Record, Transcribe, TTS)
│   ├── image.py        # 🖼️ Image Processing (Encode, Decode)
│   ├── stt.py          # 🗣️ Speech to Text Conversion
│   ├── tts.py          # 🔊 Text to Speech Conversion
│
├── services/           # 🔗 External API Integrations
│   ├── groq_client.py   # 🤖 Groq API (Vision & Text AI)
│   ├── tts_service.py  # 🎤 ElevenLabs TTS API
│
├── interfaces/         # 🎨 User Interaction & UI
│   ├── gradio_interface.py # 🌐 Gradio Chatbot UI

```


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
3. Run app/main.py



# 🏗️ Smart Medical Chatbot - Tech Stack

## ⚙️ Backend
- **FastAPI** – High-performance web framework for the chatbot API.

## 🧠 AI & NLP
- **Groq API** – Used for text and image-based AI responses.
- **SpeechRecognition** – Converts user speech to text (STT).
- **ElevenLabs API** – Optional TTS service for high-quality speech synthesis.

## 🎙️ Audio Processing
- **Pydub** – Audio file handling and conversion.
- **pyaudio** – Capturing and processing real-time audio input.

## 🖼️ Image Processing
- **Pillow (PIL)** – Image handling and processing.
- **Base64 Encoding** – Converts images to base64 for API requests.

## 🎛️ User Interface
- **Gradio** – Web-based chatbot UI with text and voice input support.

## 🛠️ Utilities & Config
- **Pydantic** – Data validation and settings management.
- **python-dotenv** – Loads environment variables from `.env` file.
- **Requests** – Handles HTTP API requests.
- **Aiohttp** – Async HTTP requests for better performance.

## 📦 Package Management
- **pip** – Python package manager.
- **pipwin** – Helps install Windows dependencies (e.g., pyaudio).

## 🌐 Deployment
- **Gradio Share Link** – Enables public access to the chatbot UI.
- **Google Cloud Platform (GCP)** – Potential cloud hosting and API integrations.

