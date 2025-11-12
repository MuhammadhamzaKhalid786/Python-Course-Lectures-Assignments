# ==========================
# MetaLearn Smart Assistant
# Module: chatbot_module.py
# ==========================

# Chatbot class to handle logic and responses

class SmartAssistant:
    def __init__(self, user_name):
        self.user_name = user_name

        # 10 total questions: 5 general + 5 Python related
        self.qa_pairs = {
            # General Questions
            "your name": "I am MetaLearn Smart Assistant, your learning buddy!",
            "how are you": "I'm doing great, thank you for asking!",
            "who created you": "I was created by a Python student for the MetaLearn Final Project.",
            "what can you do": "I can answer basic questions and make learning more fun.",
            "thank you": "You're most welcome! I'm happy to help.",

            # Python Related Questions
            "what is python": "Python is a high-level programming language used for AI, web apps, and more.",
            "who made python": "Python was created by Guido van Rossum in 1991.",
            "why learn python": "Because it's easy to learn and very powerful — perfect for beginners!",
            "what can we do with python": "You can build websites, apps, games, and even robots with Python!",
            "is python easy": "Yes! Python has simple syntax that reads almost like English."
        }

    def get_response(self, user_input):
        """Match user input with known questions."""
        user_input = user_input.lower()
        for question, answer in self.qa_pairs.items():
            if question in user_input:
                return answer
        return "I'm sorry, I don’t understand that. Can you try asking something else?"
