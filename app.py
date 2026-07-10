from tools import tools, handle_tool_call
from context import TWIN_SYSTEM_PROMPT
import gradio as gr
from style import CSS, JS, EXAMPLES
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv(override=True)
Gemini_API_KEY = os.getenv('Gemini_API_KEY')


gemini = OpenAI(
    api_key= Gemini_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
MODEL_NAME = "gemini-2.5-flash-lite"
system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = gemini.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_call(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = gemini.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":

    demo = gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )

    demo.launch(inbrowser=True)