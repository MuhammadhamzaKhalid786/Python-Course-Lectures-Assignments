# ====================================
# MetaLearn Smart Assistant - main.py
# ====================================

from MetaLearn_Assistant_Chatbot.chatbot_module import SmartAssistant

def main():
    print("=========================================")
    print("Welcome to MetaLearn Smart Assistant")
    print("=========================================")
    user_name = input("Please enter your name: ")
    bot = SmartAssistant(user_name)

    print(f"\nHello {user_name}! Type 'bye' or 'exit' anytime to quit.")
    print("Let's start chatting!\n")

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Assistant: Goodbye! Take care 😊")
            break
        response = bot.get_response(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
