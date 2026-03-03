import gradio as gr
from app.services.streaming import stream_response
from app.models import ModelProvider


def launch_gradio_ui(): 

    message_input = gr.Textbox(label="Enter your message", placeholder="Type your message here...")
    model_selection = gr.Dropdown(
        label="Select Model",
        choices=["gemini", "claude"],
        value="claude"
    )
    response_output = gr.Textbox(label="Model Response", placeholder="Model response will appear here...", interactive=False)   
    view = gr.Interface(
        fn=stream_response,
        inputs=[ model_selection, message_input],
        outputs=response_output,
        title="LLM Streaming Demo",
        description="Enter a message and select a model to see the streaming response in real-time.",
        examples=[
            [ModelProvider.GEMINI.value, "Explain the Transformer architecture in simple terms."],
            [ModelProvider.CLAUDE.value, "What are the key differences between LSTM and Transformer models?"]
        ]
    )
    view.launch(inbrowser=True)

