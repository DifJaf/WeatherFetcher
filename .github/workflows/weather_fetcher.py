#!/usr/bin/env python3
import requests
import os
from datetime import datetime

# Load API key from environment
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Singapore")
LOG_FILE = "weather_log.txt"

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        log = f"[{datetime.now()}] Error: {data.get('message', 'Unknown error')}"
    else:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        log = f"[{datetime.now()}] {CITY}: {weather}, {temp}°C"

    with open(LOG_FILE, "a") as f:
        f.write(log + "\n")

if __name__ == "__main__":
    fetch_weather()
