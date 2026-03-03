from enum import Enum

class ModelProvider(str, Enum):
    CLAUDE = "claude"
    GEMINI = "gemini"

    