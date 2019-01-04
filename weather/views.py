import requests
from django.shortcuts import render
from .models import City

def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=45e86a0a63d11da27b8a03dc4e474f69'
	
	cities = City.objects.all()
	weather_data = []

	for city in cities:

		r = requests.get(url.format(city)).json()
		city_weather = {
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon']
		}
		weather_data.append(city_weather)

	context = {'city_weather': weather_data}
	return render(request, 'weather/weather.html', context)
