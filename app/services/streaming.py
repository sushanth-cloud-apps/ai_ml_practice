from ..llm_client_factory import LlmClientFactory
from ..settings import settings

def stream_response(model, user_prompt):
    messages = [
        {"role": "system", "content": "You are an assistant."},
        {"role": "user", "content": user_prompt}
    ]
    try:
        client = LlmClientFactory.get_client(model)
        response = client.chat.completions.create(
            model=settings.GEMINI_MODEL_NAME if model.lower() == "gemini" else settings.CLAUDE_BASE_MODEL,
            messages=messages,
            stream=True
        )
        for chunk in response:
            content = getattr(chunk.choices[0].delta, "content", None)
            if content:
                yield content
    except Exception as e:
        yield f"Error: {str(e)}"


