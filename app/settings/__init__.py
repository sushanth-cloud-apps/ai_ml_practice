from functools import lru_cache
from pathlib import Path
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, AnyUrl

# Environment selection (DEV/PROD/TEST)
ENV = os.getenv("ENV", "DEV")

env_file_mapping = {
    "DEV": ".env.dev",
    "PROD": ".env.prod",
    "TEST": ".env.test",
}

# Base directory of the package
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to the config directory's env file, e.g. app/config/.env.dev
ENV_FILE_PATH = BASE_DIR / "config" / f".env.{ENV.lower()}"

print(f"Loading settings from base dir: {BASE_DIR}")
print(f"Resolved env file path: {ENV_FILE_PATH}")

# Choose an env file to use: prefer the resolved one if it exists
env_file_to_use = str(ENV_FILE_PATH) if ENV_FILE_PATH.exists() else env_file_mapping.get(ENV, ".env.dev")


class Settings(BaseSettings):
    """Application settings loaded from environment or env file."""

    GOOGLE_API_KEY: str = Field(..., env="GOOGLE_API_KEY")
    GEMINI_BASE_URL: str = Field(
        "https://gemini.googleapis.com/v1", env="GEMINI_BASE_URL"
    )
    GEMINI_MODEL_NAME: str = Field("gemini-2.5-flash", env="GEMINI_MODEL_NAME")
    max_retries: int = Field(3, env="MAX_RETRIES")

    model_config = SettingsConfigDict(
        env_file=env_file_to_use,
        env_file_encoding="utf-8",
        extra="ignore" 
    )


@lru_cache()
def get_settings() -> Settings:
    """Return a cached Settings instance.

    Raises:
        pydantic.ValidationError: if required settings are missing or invalid.
    """
    return Settings()


# Do not instantiate settings at import time to avoid hard failures during import.
settings = get_settings()