import os
import requests
from django.shortcuts import render

WEATHER_EMOJIS = {
    '01': '☀️',
    '02': '⛅',
    '03': '☁️',
    '04': '☁️',
    '09': '\U0001f327️',
    '10': '\U0001f327️',
    '11': '⛈️',
    '13': '❄️',
    '50': '\U0001f32b️',
}


def home(request):
    temperature = None
    weather_description = None
    weather_emoji = None

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
        icon_code = data['weather'][0]['icon']
        weather_emoji = WEATHER_EMOJIS.get(icon_code[:2], '')

    context = {
        'temperature': temperature,
        'weather_description': weather_description,
        'weather_emoji': weather_emoji,
    }
    return render(request, 'index.html', context)


def map_page(request):
    return render(request, 'map.html')


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')


def add_cafe_page(request):
    return render(request, 'add-cafe.html')
