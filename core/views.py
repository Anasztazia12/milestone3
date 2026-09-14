import os
import requests
from django.shortcuts import render


def home(request):
    temperature = None
    weather_description = None

    api_key = os.environ.get('WEATHER_API_KEY')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': 'London',
        'appid': api_key,
        'units': 'metric',
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

    context = {
        'temperature': temperature,
        'weather_description': weather_description,
    }
    return render(request, 'index.html', context)
