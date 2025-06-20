def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "your name" in user_input:
        return "I'm ChatBot, your assistant!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

# Main chatbot loop
print("ChatBot: Hello! Type 'bye' to end the chat.")
while True:
    user_message = input("You: ")
    if user_message.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    reply = chatbot_response(user_message)
    print("ChatBot:", reply)
