from django.shortcuts import render
import requests

def format_timezone(offset_seconds):
    hours = offset_seconds // 3600
    return f"UTC{'+' if hours >= 0 else ''}{hours}"

def index(request):
    return render(request, 'app/index.html')

def get_weather(request):
    city = request.POST.get("city_name", "")
    weather_data = None

    if city:
        api_key = "cab1ab860ac33e46e4db8cfbb226ff58"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == 200:
            weather_data = {
                "location": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "weather": data["weather"][0]["main"],
                "icon": data["weather"][0]["icon"],
                "wind_speed": data["wind"]["speed"],
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "timezone": format_timezone(data["timezone"]),
            }
        else:
            weather_data = {"error": data.get("message").capitalize()}

    return render(request, "app/index.html", {"weather": weather_data})