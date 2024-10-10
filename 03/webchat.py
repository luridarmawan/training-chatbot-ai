import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

def respond(message, chat_history):
    
    answer = "test jawab dari: " + message
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

    send_button.click(respond, 
        inputs=[message_box, chatbot],
        outputs=[chatbot, message_box])
    message_box.submit(respond, 
        inputs=[message_box, chatbot],
        outputs=[chatbot, message_box])

PORT = os.getenv('APP_PORT', 8088)
PORT = int(PORT)
demo.launch(share=False, show_api=True, server_port=PORT)
