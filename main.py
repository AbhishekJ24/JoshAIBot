from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File
from responses import get_response

# STEP 0: LOADING OUR TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return
    
    
    if is_private := user_message[0]=='?':
        user_message=user_message[1:]

    try:
        response: str = get_response(user_message)
        if response.endswith(".jpg"):
            meme_path = response
            if os.path.exists(meme_path):
                if is_private:
                    await message.author.send(file=File(meme_path))
                else:
                    await message.channel.send(file=File(meme_path))
            else:
                print(f"File not found: {meme_path}")

        else:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
                
    except Exception as e:
        print(e)


# STEP 3: HANDLING STARTUP FOR BOT
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now working")


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f"[{channel}] {username} {user_message}")
    await send_message(message,user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()