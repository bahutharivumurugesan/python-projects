print("🤖 Simple AI Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I'm fine!")

    elif user == "your name":
        print("Bot: I'm a Python chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")