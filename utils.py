import json
from discord.ext.commands import Bot
from os import listdir

def get_prefix(client, message):
    with open('data/server_prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes.get(str(message.guild.id), 'bl!')  # Default prefix

def add_guild_prefix(guild_id):
    with open('data/server_prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild_id)] = 'bl!'  # Default prefix

    with open('data/server_prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

def remove_guild_prefix(guild_id):
    with open('data/server_prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild_id), None)

    with open('data/server_prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

async def load_extensions(bot : Bot):
    for filename in listdir('./cogs'):
        if filename.endswith('.py') and filename != 'utils.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded cog: cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load cog cogs.{filename[:-3]}: {e}")
