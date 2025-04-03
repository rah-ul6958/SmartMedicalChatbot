import logging
import speech_recognition as sr
from pathlib import Path

def record_audio_from_mic(timeout: int = 5, phrase_time_limit: int = 10) -> str:
    """
    Records audio from the microphone and saves it as a WAV file.
    
    :param timeout: Seconds to wait for a phrase to start.
    :param phrase_time_limit: Maximum seconds of recording.
    :return: Path to the saved WAV file.
    """
    recognizer = sr.Recognizer()
    wav_filepath = "recorded_audio.wav"
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Recording audio from microphone...")
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            with open(wav_filepath, "wb") as f:
                f.write(audio_data.get_wav_data())
            logging.info(f"Audio recorded and saved to {wav_filepath}")
    except Exception as e:
        logging.error(f"Error recording audio: {e}")
    return wav_filepath

def transcribe_audio(audio_path: str, language: str = "en-US") -> str:
    """
    Transcribes an audio file using the Google Web Speech API (via speech_recognition).
    
    :param audio_path: Path to the audio file (WAV format is recommended).
    :param language: Language code for transcription.
    :return: Transcribed text.
    """
    recognizer = sr.Recognizer()
    transcript = ""
    try:
        if not Path(audio_path).exists():
            logging.error(f"Audio file not found: {audio_path}")
            return ""
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            transcript = recognizer.recognize_google(audio_data, language=language)
            logging.info(f"Transcription result: {transcript}")
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
    return transcript
