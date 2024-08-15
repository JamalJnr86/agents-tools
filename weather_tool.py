#weather_tool.py
import requests #type: ignore

def get_weather(city):
    api_key = "8ac63e8a7710b32933857343e1bc5206"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
        return f"The weather in {city} is {weather} with a temperature of {temperature:.2f}°C."
    else:
        return "Could not fetch weather data."
