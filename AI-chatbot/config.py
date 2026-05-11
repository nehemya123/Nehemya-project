def get_system_prompt(tone):
    if tone == "Casual":
        return "You are a chill chatbot. Speak casually. Profanity is allowed."
    elif tone == "Professional":
        return "You are a professional assistant. Be clear and formal."
    else:
        return "You are a helpful assistant. Be natural and conversational."