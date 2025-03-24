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

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != 'utils.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded cog: cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load cog cogs.{filename[:-3]}: {e}")

@bot.event
async def setup_hook():
    await load_extensions()

bot.run(os.getenv('DISCORD_BOT_TOKEN'))