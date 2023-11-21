import discord
from discord import Intents
import os
from dotenv import load_dotenv
from weather_api import get_weather

# Load environment variables from .env file
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

    if message.content.startswith('$weather'):
        city = message.content.split('$weather ', 1)[1]

        try:
            weather_data = get_weather(city, os.getenv('WEATHER_API_KEY'))
            description = weather_data['current']['condition']['text']
            temperature = weather_data['current']['temp_c']
            await message.channel.send(f"Weather in {city}: {description}, {temperature}°C")
        except KeyError:
            await message.channel.send("Could not find weather data for this city.")
        except Exception as e:
            await message.channel.send("An error occurred.")
            print(e)  # Log the error to console for debugging


client.run(os.getenv('DISCORD_BOT_TOKEN'))