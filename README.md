# ai_ml_practice
projects_related_to_AIML and LLMs
# Agentic AI — LLM Streaming Demo

Lightweight demo app showing streaming responses from LLM providers (Gemini / Claude) via a simple Gradio UI.

## Requirements
- Python 3.10+
- See [requirements.txt](requirements.txt) for dependencies.

## Setup
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Configure environment variables:

- Copy the example env file and fill in keys:

[app/config/.env.example](app/config/.env.example)

The project expects env variables such as:

- `GOOGLE_API_KEY` — API key for Gemini (Google).
- `CLAUDE_API_KEY` — API key for Claude (if used).
- Optional: `GEMINI_BASE_URL`, `CLAUDE_BASE_URL`, `GEMINI_MODEL_NAME`, `MAX_RETRIES`.

Environment files are resolved by the settings module; dev/prod/test selection is driven by the `ENV` environment variable.

## Running the app

Launch the Gradio UI locally:

```bash
# from project root
python -m app.main
```

This opens a browser with the streaming demo.

## Notes
- The code currently uses the `openai` client as a placeholder for multiple providers — see `app/llm_client_factory.py`.
- Streaming is implemented in `app/services/streaming.py` and consumed by the Gradio interface at `app/ui/gradio_ui.py`.

## Troubleshooting
- If imports fail, ensure the virtualenv is activated and `requirements.txt` is installed.
- Check that the selected `.env` file exists and contains required variables.

## Contributing
- Open an issue or send a PR. Keep changes minimal and include tests where appropriate.

## License
MIT