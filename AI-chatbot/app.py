import gradio as gr
from chatbot import get_response
from config import get_system_prompt

messages = []

def chat(user_input, history, tone):
    global messages

    # Add system prompt once
    if len(messages) == 0:
        messages.append({
            "role": "system",
            "content": get_system_prompt(tone)
        })

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Get AI response
    reply = get_response(messages)

    # Add assistant message
    messages.append({
        "role": "assistant",
        "content": reply
    })

    # Only show user + assistant messages
    visible_history = [
        msg for msg in messages
        if msg["role"] != "system"
    ]

    return visible_history, visible_history

with gr.Blocks() as app:

    gr.Markdown("Local AI Chatbot")

    tone = gr.Dropdown(
        ["Casual", "Professional", "Balanced"],
        value="Balanced",
        label="Tone"
    )

    chatbot_ui = gr.Chatbot()

    state = gr.State([])

    msg = gr.Textbox(
        placeholder="Type a message..."
    )

    msg.submit(
        chat,
        [msg, state, tone],
        [chatbot_ui, state]
    )

app.launch()