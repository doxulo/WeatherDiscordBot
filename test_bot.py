import discord
from discord import Intents
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up intents
intents = Intents.all()

# Initialize Discord client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$test':
        await message.channel.send('Test successful!')

client.run(os.getenv('DISCORD_BOT_TOKEN'))
