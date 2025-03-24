from discord.ext import commands
import os
from weather_api import *
from .utils import get_location_string

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather')
    async def weather(self, ctx, *, city: str):
        try:
            weather_data = get_weather(city, os.getenv('WEATHER_API_KEY'))
            location_string = get_location_string(weather_data)
            description = weather_data['current']['condition']['text']
            temperature = weather_data['current']['temp_c']

            await ctx.send(f"Weather in {location_string}: {description}, {temperature}°C")
        except KeyError:
            await ctx.send("Could not find weather data for this city.")
        except Exception as e:
            await ctx.send("An error occurred.")
            print(e)  # Log the error to console for debugging

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

    @commands.command(name='alerts')
    async def alerts(self, ctx, *, city: str):
        try:
            alerts_data = get_alerts(city, os.getenv('WEATHER_API_KEY'))
            location_string = get_location_string(alerts_data)

            if alerts_data['alerts']['alert']:
                alerts_message = f"Weather alerts for {location_string}:\n"
                for alert in alerts_data['alerts']['alert']:
                    headline = alert['headline']
                    msgtype = alert['msgtype']
                    severity = alert['severity']
                    certainty =  alert['certainty']
                    effective = alert['effective']
                    expires = alert['expires']
                    description = alert['desc']
                    instruction = alert['instruction']
                    alerts_message += f"Headline: {headline}\nMsgType: {msgtype}\nSeverity: {severity}\nCertainty: {certainty}\nEffective: {effective}\nExpires: {expires}\nDescription: {description}\nInstruction: {instruction}\n\n"
                await ctx.send(alerts_message)
            else:
                await ctx.send(f"No weather alerts found for {location_string}.")

        except KeyError:
            await ctx.send("Could not find weather data for this city.")
        except Exception as e:
            await ctx.send("An error occurred.")
            print(e)  # Log the error to console for debugging

async def setup(bot):
    await bot.add_cog(Weather(bot))