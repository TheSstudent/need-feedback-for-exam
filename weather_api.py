import requests
from datetime import datetime

api_key = 'b4189d53714a61b68fe0a6d8cc29619e'


def get_forecast(lon, lat):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    x = response.json()

    temperatures = []
    types = []
    times = []
    for i in range(6):
        temperature = x["list"][i]["main"]["temp"]
        time = x["list"][i]["dt_txt"]
        weather_type = x["list"][i]["weather"][0]["main"]
        temperatures.append(temperature)
        times.append(datetime.fromisoformat(time))
        types.append(weather_type)

    return temperatures, types, times