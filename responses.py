from random import choice, randint

def get_response(user_input: str) -> str:
    
    lowered: str = user_input.lower()

    if(lowered==""):
        return "Why the silence, is it somebody's funeral??"
    
    elif(lowered.startswith("hello")):
        return "Well, hello there, how do I assist you"
    
    elif(lowered.startswith("bye") or lowered.startswith("thanks")):
        return "Happy to assist you, have a great day ahead"
    
    elif(lowered=="roll" or lowered=="roll dice" or lowered=="roll the dice"):
        return f"Rolling dice....\n{randint(1,6)}"
    
    else:
        return choice(["I don't understand", 
                       "What are you talking about", 
                       "Do you mind rephrasing that", 
                       "Are you nuts"])