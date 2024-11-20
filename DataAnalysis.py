import requests

def get_weather(location="Berlin"):
    """Holt Wetterdaten für den angegebenen Ort."""
    API_KEY = "deine_openweathermap_api_key"  # Registriere dich bei openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {location} is {weather} with a temperature of {temp}°C."
    else:
        return "I couldn't retrieve the weather data."
