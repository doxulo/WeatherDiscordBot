import discord
from discord import Intents
from discord.ext import commands
import os
from dotenv import load_dotenv
from weather_api import get_weather, get_forecast

# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = Intents.all()

# Initialize bot with command prefix
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='weather')
async def weather(ctx, *, city: str):
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

@bot.command(name='forecast')
async def forecast(ctx, *, city: str):
    try:
        forecast_data = get_forecast(city, os.getenv('WEATHER_API_KEY'))
        name = forecast_data['location']['name']
        country = forecast_data['location']['country']

        forecast_message = f"Weather forecast for {name}, {country}:\n"
        for day in forecast_data['forecast']['forecastday']:
            date = day['date']
            condition = day['day']['condition']['text']
            max_temp = day['day']['maxtemp_c']
            min_temp = day['day']['mintemp_c']
            forecast_message += f"{date}: {condition}, {min_temp}°C - {max_temp}°C\n"

        await ctx.send(forecast_message)
    except KeyError:
        await ctx.send("Could not find forecast data for this city.")
    except Exception as e:
        await ctx.send("An error occurred.")
        print(e)  # Log the error to console for debugging

bot.run(os.getenv('DISCORD_BOT_TOKEN'))