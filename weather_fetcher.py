#!/usr/bin/env python3
# WEATHER FETCHER SCRIPT — API Secured & Hybrid-Deployable

import requests
import os
from datetime import datetime

# Constants
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Stored securely
CITY = "Singapore"
URL_TEMPLATE = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

def fetch_weather(city: str) -> dict:
    url = URL_TEMPLATE.format(city, API_KEY)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch weather: {e}")
        return {}

def parse_weather(data: dict) -> str:
    if "main" in data and "weather" in data:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"Weather in {CITY}: {description}, {temp}°C"
    return "[ERROR] Invalid weather data."

def log_weather():
    weather_data = fetch_weather(CITY)
    report = parse_weather(weather_data)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{now} — {report}\n"

    with open("weather_log.txt", "a") as log_file:
        log_file.write(log_line)
    print(log_line)

if __name__ == "__main__":
    log_weather()
