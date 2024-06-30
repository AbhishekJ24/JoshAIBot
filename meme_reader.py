import os
from random import choice

def read_memes() -> str:
    meme_dir = "/Users/gamingspectrum24/Documents/PRG/Projects/Generic/JoshAIBot/assets/memes/"
    entries = os.listdir("assets/memes")
    if entries:
        return os.path.join(meme_dir, choice(entries))
    else:
        return "No memes available"