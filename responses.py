from random import choice, randint
from meme_reader import read_memes

def get_response(user_input: str) -> str:
    cleaned_input = user_input.strip().lower()
    
    if not cleaned_input:
        return "Why the silence? Is it somebody's funeral?"
    
    if cleaned_input.endswith("?"):
        return "I'd like to apologize but I am not yet trained on ML models to generate output."
    
    greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "hola", "howdy"]
    farewells = ["bye", "thanks"]
    
    for greeting in greetings:
        if cleaned_input.startswith(greeting):
            return "Well, hello there, how may I assist you?"
    
    for farewell in farewells:
        if cleaned_input.startswith(farewell):
            return "Happy to assist you, have a great day ahead."
    
    if cleaned_input in ["roll", "roll dice", "roll the dice"]:
        return f"Rolling dice....\n{randint(1, 6)}"
    
    if cleaned_input == "meme":
        try:
            return read_memes()
        except Exception as e:
            return f"Error reading memes: {str(e)}"
    
    return choice(["I don't understand", "What are you talking about", "Do you mind rephrasing that?", "Are you nuts?"])
