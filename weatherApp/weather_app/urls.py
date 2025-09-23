from django.urls import path
from . import views

urlpatterns=[
    path('',views.form,name='form'),
    path('weather_data',views.weather_data,name='weather'),
]