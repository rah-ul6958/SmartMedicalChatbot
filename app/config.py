from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GROQ_API_KEY: str = Field(..., env="GROQ_API_KEY")
    ELEVENLABS_API_KEY: str = Field(..., env="ELEVENLABS_API_KEY")
    IMAGE_MODEL: str = "llama-3.2-11b-vision-preview"
    SPEECH_MODEL: str = "whisper-large-v3"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

if __name__ == "__main__":
    print("Loaded configuration:")
    print(f"GROQ_API_KEY: {settings.GROQ_API_KEY}")
    print(f"ELEVENLABS_API_KEY: {settings.ELEVENLABS_API_KEY}")
    print(f"IMAGE_MODEL: {settings.IMAGE_MODEL}")
    print(f"SPEECH_MODEL: {settings.SPEECH_MODEL}")
