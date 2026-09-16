import os
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

WEATHER_ICONS = {
    '01': 'bi-sun',
    '02': 'bi-cloud-sun',
    '03': 'bi-clouds',
    '04': 'bi-clouds',
    '09': 'bi-cloud-rain',
    '10': 'bi-cloud-rain-heavy',
    '11': 'bi-cloud-lightning-rain',
    '13': 'bi-snow',
    '50': 'bi-cloud-fog2',
}

WEATHER_COLORS = {
    '01': 'weather-sun',
    '02': 'weather-cloud',
    '03': 'weather-overcast',
    '04': 'weather-overcast',
    '09': 'weather-rain',
    '10': 'weather-rain',
    '11': 'weather-storm',
    '13': 'weather-snow',
    '50': 'weather-mist',
}


def home(request):
    temperature = None
    weather_description = None
    weather_icon_class = None
    weather_color_class = None
    city = request.GET.get('city', 'London')

    api_key = os.environ.get('WEATHER_API_KEY')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        weather_icon_class = WEATHER_ICONS.get(icon_code[:2], 'bi-cloud')
        weather_color_class = WEATHER_COLORS.get(icon_code[:2], 'weather-cloud')

    context = {
        'city': city,
        'temperature': temperature,
        'weather_description': weather_description,
        'weather_icon_class': weather_icon_class,
        'weather_color_class': weather_color_class,
    }
    return render(request, 'index.html', context)


def map_page(request):
    return render(request, 'map.html')


def login_page(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Wrong username or password'

    return render(request, 'login.html', {'error': error})


def signup_page(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error = 'Passwords do not match'
        elif User.objects.filter(username=username).exists():
            error = 'Username already taken'
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('home')

    return render(request, 'signup.html', {'error': error})


def logout_page(request):
    logout(request)
    return redirect('home')


def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('home')

    return render(request, 'delete_account.html')


def add_cafe_page(request):
    return render(request, 'add-cafe.html')
