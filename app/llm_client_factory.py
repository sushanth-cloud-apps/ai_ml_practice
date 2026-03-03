
from .models import ModelProvider
from .settings import settings
from openai import OpenAI

class LlmClientFactory:

  @staticmethod
  def get_client(model_provider: ModelProvider) -> OpenAI:
        if model_provider.lower() == ModelProvider.GEMINI:
           return OpenAI(api_key=settings.GOOGLE_API_KEY, base_url=settings.GEMINI_BASE_URL)
        elif model_provider.lower() == ModelProvider.CLAUDE.value:
            # Return Claude client instance
            return OpenAI(api_key=settings.CLAUDE_API_KEY, base_url=settings.CLAUDE_BASE_URL)  # Placeholder for actual Claude client
        else:
            raise ValueError(f"Unsupported model provider: {model_provider}")
        