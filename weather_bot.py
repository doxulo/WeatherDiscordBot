import json
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils import get_prefix, add_guild_prefix, remove_guild_prefix, load_extensions  # Import utility functions

# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = discord.Intents.all()

# Initialize bot with command prefix
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='guilds', help='Get a list of guilds the bot is in')
@commands.is_owner()
async def guilds(ctx):
    guild_list = '\n'.join([
        f"{guild.name} (ID: {guild.id})"
        for guild in bot.guilds
    ])
    await ctx.send(f"The bot is in the following guilds:\n{guild_list}")

@bot.event
async def setup_hook():
    await load_extensions(bot)

@bot.event
async def on_guild_join(guild):
    add_guild_prefix(guild.id)

@bot.event
async def on_guild_remove(guild):
    remove_guild_prefix(guild.id)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('data/server_prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('data/server_prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

token = os.getenv('DISCORD_BOT_TOKEN')
if token:
    bot.run(token)
else:
    print("DISCORD_BOT_TOKEN not found in environment variables")