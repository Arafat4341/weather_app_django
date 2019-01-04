import requests
from django.shortcuts import render

def index(request):
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=45e86a0a63d11da27b8a03dc4e474f69'
	city = 'Dhaka'
	r = requests.get(url.format(city)).json()
	city_weather = {
		'city': city,
		'temperature': r['main']['temp'],
		'description': r['weather'][0]['description'],
		'icon': r['weather'][0]['icon']
	}
	return render(request, 'weather/weather.html')
