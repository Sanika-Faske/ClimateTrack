from django.shortcuts import render
import requests
import datetime

def home(request):
    if request.method == "POST":
        city = request.POST.get('city')
    else:
        city = 'Kolhapur'  # default city

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e0c893d6f2e3be62b6a8533a3ca2b24a'
    PARAMS = {'units': 'metric'}

    data = requests.get(url, params=PARAMS).json()

    context = {'city': city, 'day': datetime.date.today()}

    if data.get('cod') == 200: 
        context['description'] = data['weather'][0]['description']
        context['icon'] = data['weather'][0]['icon']
        context['temp'] = data['main']['temp']
    else: 
        context['error'] = data.get('message', 'City not found!')

    return render(request, 'index.html', context)
