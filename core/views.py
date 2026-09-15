import os
import requests
from django.shortcuts import render


def home(request):
    temperature = None
    weather_description = None
    weather_icon = None

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
        weather_icon = data['weather'][0]['icon']

    context = {
        'temperature': temperature,
        'weather_description': weather_description,
        'weather_icon': weather_icon,
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
