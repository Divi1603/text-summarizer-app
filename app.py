import gradio as gr
from transformers import pipeline

# Load model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# UI
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Paste your text here..."),
    outputs="text",
    title="AI Text Summarizer",
    description="Paste long text and get a short summary"
)

interface.launch()