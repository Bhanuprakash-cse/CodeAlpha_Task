def chatbot():
    print("🤖 Chatbot: Hello! Type something to start (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")    
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand.")

# Start the chatbot
chatbot()
