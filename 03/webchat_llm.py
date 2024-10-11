import os
import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

messages = [
    ("system", "kamu adalah asisten AI pintar.")
]

model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI( model=model)

def respond(message, chat_history):
    messages.append(("human", message))
    result = llm.invoke(messages)
    messages.append(("ai", result.content))

    answer = result.content
    chat_history.append(("User", message))
    chat_history.append(("Bot", answer))

    return chat_history, ""

with gr.Blocks() as demo:
    gr.Markdown("<h1>Web Chat BPS</h1>")

    chatbot = gr.Chatbot()

    with gr.Row():
        with gr.Column():
            message_box = gr.Textbox(
                show_label=False, placeholder="Ketik pesan anda di sini", lines=1
            )
        with gr.Column():
            send_button = gr.Button("Kirim")
        
    with gr.Row():
        gr.File(file_count="multiple")

    send_button.click(respond, 
        inputs=[message_box, chatbot],
        outputs=[chatbot, message_box])
    message_box.submit(respond, 
        inputs=[message_box, chatbot],
        outputs=[chatbot, message_box])

PORT = os.getenv('APP_PORT', 8088)
PORT = int(PORT)
demo.launch(share=False, show_api=True, server_port=PORT)
