# Weather Discord Bot

This is a simple Discord bot that provides weather information based on user queries.

## Features

-   Retrieves and displays current weather data for a specified city.
-   Displays city name, country, weather description, and temperature in Celsius.
-   Handles invalid city names and API errors gracefully.

## Prerequisites

-   Python 3.6+
-   Discord bot token
-   WeatherAPI.com API key

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**

    ```bash
    pip install discord.py python-dotenv requests
    ```

4.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your Discord bot token and WeatherAPI.com API key:

    ```
    DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
    WEATHER_API_KEY=YOUR_WEATHER_API_KEY
    ```

    -   Replace `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token.
    -   Replace `YOUR_WEATHER_API_KEY` with your WeatherAPI.com API key, which you can get from [https://www.weatherapi.com/](https://www.weatherapi.com/).

5.  **Run the bot:**

    ```bash
    python weather_bot.py
    ```

## Usage

In your Discord server, use the following command to get weather information:

$weather <city_name>


For example:

$weather London


The bot will respond with the current weather information for the specified city.

## Code Explanation

-   `discord.py`: Used for interacting with the Discord API.
-   `python-dotenv`: Used for loading environment variables from the `.env` file.
-   `requests`: Used for making HTTP requests to the WeatherAPI.com API.
-   `weather_api.py` (assumed to be included within the same directory): contains the `get_weather` function that makes the api call and parses the json.
-   The bot listens for messages starting with `$weather`.
-   It extracts the city name from the message and calls the `get_weather` function to retrieve weather data.
-   It sends the weather information back to the Discord channel.
-   Error handling is implemented to gracefully handle invalid city names and API errors.
-   All intents are enabled to allow for maximum functionality.
-   Error messages are printed to the console for debugging purposes.

## Dependencies

-   `discord.py`
-   `python-dotenv`
-   `requests`