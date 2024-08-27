from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page where the user enters the date range
    path('weather-graphs/', views.weather_graphs, name='weather_graphs'),  # Page to display the graphs
]
