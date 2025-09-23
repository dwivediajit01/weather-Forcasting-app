from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse 
from .utils_conversion import *
    

# Create your views here.

def form(request):
    if request.method=='POST':
        weather_forcast = request.POST.get('choice')
        # print(weather_forcast)
        request.session['weather_forcast']=weather_forcast
        form_select = request.POST.get('form_select')
        request.session['form_select']=form_select


        if form_select=='form_1':
            longitude=request.POST.get("longitude")
            latitude=request.POST.get("latitude")
            request.session['longitude']=longitude
            request.session['latitude']=latitude


        elif form_select=='form_2':
            city_name=request.POST.get("city_name")
            country_code=request.POST.get("country_code")
            request.session['city_name']=city_name
            request.session['country_code']=country_code


        elif form_select =='form_3':
            name = request.POST.get("place_name")
            request.session['name']=name
        return redirect(weather_data)
    return render(request,'weather_app/form.html')

def weather_data(request):
    API_key='ce2f54623e14e468d3a2d18a0c746929'
    lon=request.session.get('longitude')
    lat=request.session.get('latitude')
    city_name=request.session.get('city_name')
    country_code=request.session.get('country_code')
    name=request.session.get('name')
    form_select=request.session.get('form_select')
    weather_forcast=request.session.get('weather_forcast')

    if weather_forcast == 'daily_forcast':
        flag='daily_forcast'
        if form_select == 'form_1':
            url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
        elif form_select == 'form_2':
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_key}'
        elif form_select == 'form_3':
            url=f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={API_key}'
        else:
            return redirect(form)
        
        res=requests.get(url)
        a=res.json()
        context={
            'lon':a['coord']['lon'],
            'lat':a['coord']['lat'],
            'weather':a['weather'][0]['main'],
            'weather_description':a['weather'][0]['description'],
            'temp':kelvin_to_celcious(a['main']['temp']),
            'feels_like':kelvin_to_celcious(a['main']['feels_like']),
            'temp_min':kelvin_to_celcious(a['main']['temp_min']),
            'temp_max':kelvin_to_celcious(a['main']['temp_max']),
            'pressure':a['main']['pressure'],
            'humidity':a['main']['humidity'],
            'sea_level':a['main']['sea_level'],
            'grnd_level':a['main']['grnd_level'],
            'visibility':meters_to_km(a.get('visibility','N/A')),
            'wind_speed':a['wind']['speed'],
            'wind_deg':wind_deg_to_compass(a['wind']['deg']),
            'wind_gust':a['wind']['gust'],
            'clouds':a['clouds']['all'],
            'dt':unix_to_localtime(a['dt'],a['timezone']),
            'country':a['sys']['country'],
            'sunrise':unix_to_localtime(a['sys']['sunrise'],a['timezone']),
            'sunset':unix_to_localtime(a['sys']['sunset'],a['timezone']),
            'timezone':seconds_to_timezone(a['timezone']),
            'city_name':a['name'],
        }
    elif weather_forcast == '5-day_forcast':
        flag='5-day_forcast'
        if form_select == 'form_1':
            url=f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'
        elif form_select == 'form_2':
            url=f'https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={API_key}'
        elif form_select == 'form_3':
            url=f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}'
        else:
            return redirect(form)
        
        res=requests.get(url)
        a=res.json()
        context=[]
        for i in range(0,len(a['list'])-1):
            dt=a['list'][i]['dt_txt']
            date,time=dt.split(' ')
            context.append({
                'date':date,
                'time':time,
                'weather':a['list'][i]['weather'][0]['main'],
                'weather_description':a['list'][i]['weather'][0]['description'],
                'temp':kelvin_to_celcious(a['list'][i]['main']['temp']),
                'feels_like':kelvin_to_celcious(a['list'][i]['main']['feels_like']),
                'temp_min':kelvin_to_celcious(a['list'][i]['main']['temp_min']),
                'temp_max':kelvin_to_celcious(a['list'][i]['main']['temp_max']),
                'pressure':a['list'][i]['main']['pressure'],
                'humidity':a['list'][i]['main']['humidity'],
                'sea_level':a['list'][i]['main']['sea_level'],
                'grnd_level':a['list'][i]['main']['grnd_level'],
                'wind_speed':a['list'][i]['wind']['speed'],
                'wind_deg':wind_deg_to_compass(a['list'][i]['wind']['deg']),
                'wind_gust':a['list'][i]['wind']['gust'],
                'clouds':a['list'][i]['clouds']['all'],
            })
    
    return render(request,'home.html',{'weather':context,'flag':flag})