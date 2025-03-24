import discord
from discord.ext import commands

class MyHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog, commands in mapping.items():
            command_signatures = [self.get_command_signature(c) for c in commands]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"Help for {command.name}", description=command.description)
        if command.aliases:
            embed.add_field(name="Aliases", value=", ".join(command.aliases), inline=False)
        embed.add_field(name="Usage", value=self.get_command_signature(command), inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=f"Help for {cog.qualified_name}", description=cog.description)
        for command in cog.get_commands():
            embed.add_field(name=self.get_command_signature(command), value=command.description, inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=f"Help for {group.name}", description=group.description)
        if group.aliases:
            embed.add_field(name="Aliases", value=", ".join(group.aliases), inline=False)
        embed.add_field(name="Usage", value=self.get_command_signature(group), inline=False)
        for command in group.commands:
            embed.add_field(name=self.get_command_signature(command), value=command.description, inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

async def setup(bot):
    bot.help_command = MyHelp()
