from discord.ext import commands
import os
from weather_api import get_forecast
from .utils import get_location_string

class Forecast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='forecast')
    async def forecast(self, ctx, *, city: str):
        try:
            forecast_data = get_forecast(city, os.getenv('WEATHER_API_KEY'))
            location_string = get_location_string(forecast_data)

            forecast_message = f"Weather forecast for {location_string}:\n"
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

async def setup(bot):
    await bot.add_cog(Forecast(bot))