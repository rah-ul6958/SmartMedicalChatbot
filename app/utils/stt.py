import speech_recognition as sr
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

def record_audio(output_path: str = "recorded_audio.wav", duration: int = 5) -> str:
    """
    Records audio from the microphone and saves it as a WAV file.

    :param output_path: Path to save the recorded audio.
    :param duration: Recording duration in seconds.
    :return: The file path of the saved audio.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            logging.info("🎙 Speak now...")
            recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
            audio = recognizer.listen(source, timeout=duration)
        
        # Save recorded audio
        with open(output_path, "wb") as audio_file:
            audio_file.write(audio.get_wav_data())

        logging.info(f"✅ Audio recorded: {output_path}")
        return output_path

    except Exception as e:
        logging.error(f"❌ Error recording audio: {e}")
        return ""

def transcribe_audio(file_path: str) -> str:
    """
    Converts speech from an audio file into text using Google's Speech Recognition.

    :param file_path: Path to the audio file.
    :return: Transcribed text.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)  # Read audio file
        
        text = recognizer.recognize_google(audio)  # Use Google STT
        logging.info(f"📝 Transcribed Text: {text}")
        return text

    except sr.UnknownValueError:
        logging.warning("⚠️ Could not understand the audio.")
        return "I couldn't understand that."
    except Exception as e:
        logging.error(f"❌ Error transcribing audio: {e}")
        return ""

