from discord.ext import commands
import os
from weather_api import get_weather

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather')
    async def weather(self, ctx, *, city: str):
        try:
            weather_data = get_weather(city, os.getenv('WEATHER_API_KEY'))
            name = weather_data['location']['name']
            country = weather_data['location']['country']

            description = weather_data['current']['condition']['text']
            temperature = weather_data['current']['temp_c']
            await ctx.send(f"Weather in {name}, {country}: {description}, {temperature}°C")
        except KeyError:
            await ctx.send("Could not find weather data for this city.")
        except Exception as e:
            await ctx.send("An error occurred.")
            print(e)  # Log the error to console for debugging

async def setup(bot):
    await bot.add_cog(Weather(bot))