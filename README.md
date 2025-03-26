# Weather Discord Bot

This is a simple Discord bot that provides weather information based on user queries.

## Features

- Retrieves and displays current weather data for a specified city.
- Displays city name, country, weather description, and temperature in Celsius.
- Provides weather forecast for the next few days.
- Shows weather alerts for a specified city.
- Displays hourly weather forecast.
- Customizable command prefix for each server.
- Handles invalid city names and API errors gracefully.

## Prerequisites

- Python 3.6+
- Discord bot token
- WeatherAPI.com API key

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install dependencies:**

    ```bash
    pip install discord.py python-dotenv requests
    ```

4. **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your Discord bot token and WeatherAPI.com API key:

    ```
    DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
    WEATHER_API_KEY=YOUR_WEATHER_API_KEY
    ```

    - Replace `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token.
    - Replace `YOUR_WEATHER_API_KEY` with your WeatherAPI.com API key, which you can get from [https://www.weatherapi.com/](https://www.weatherapi.com/).

5. **Run the bot:**

    ```bash
    python weather_bot.py
    ```

## Usage

In your Discord server, use the following commands to get weather information:

- `$weather <city_name>`: Get the current weather for a city.
- `$forecast <city_name>`: Get the weather forecast for a city.
- `$alerts <city_name>`: Get weather alerts for a city.
- `$hourly <city_name>`: Get the hourly weather forecast for a city.
- `$changeprefix <new_prefix>`: Change the command prefix for the server (admin only).

For example:

```bash
$weather London
$forecast London
$alerts London
$hourly London
$changeprefix !
```

The bot will respond with the requested weather information for the specified city.

## Code Explanation

- `discord.py`: Used for interacting with the Discord API.
- `python-dotenv`: Used for loading environment variables from the `.env` file.
- `requests`: Used for making HTTP requests to the WeatherAPI.com API.
- `weather_api.py`: Contains functions to get current weather, forecast, alerts, and hourly forecast.
- `utils.py`: Contains utility functions for managing server-specific command prefixes and loading bot extensions.
- `cogs/help.py`: Custom help command for the bot.
- `cogs/weather.py`: Contains weather-related commands.

## Dependencies

- `discord.py`
- `python-dotenv`
- `requests`