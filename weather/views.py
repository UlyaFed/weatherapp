from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def index(request):
    weather_data = None
    if "city" in request.GET:
        city = request.GET["city"]
        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"],
            }
        else:
            weather_data = {"error": "City not found. Please try again."}
    return render(request, "weather/index.html", {"weather": weather_data})
