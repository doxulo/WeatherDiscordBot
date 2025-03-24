import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = discord.Intents.all()

# Initialize bot with command prefix
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load cogs
bot.load_extension('cogs.weather')
bot.load_extension('cogs.forecast')

bot.run(os.getenv('DISCORD_BOT_TOKEN'))