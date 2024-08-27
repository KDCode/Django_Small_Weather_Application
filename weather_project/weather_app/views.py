import os
import pandas as pd
import plotly.express as px
from django.conf import settings
from django.shortcuts import render,redirect
def home(request):
    if request.method == 'GET':
        return render(request, 'weather_app/home.html')
    elif request.method == 'POST':
        city = request.POST.get('city', 'Delhi')
        start_date = request.POST.get('start_date', '2020-08-01')
        end_date = request.POST.get('end_date', '2024-08-01')

        # Redirect to the weather_graphs view with the parameters
        return redirect(f'/weather-graphs/?city={city}&start_date={start_date}&end_date={end_date}')

def weather_graphs(request):
    city = request.GET.get('city', 'Delhi')
    start_date = request.GET.get('start_date', '2020-08-01')
    end_date = request.GET.get('end_date', '2024-08-01')

    # Path to the CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'weather_app', 'data', 'delhi_weather_2019_2024.csv')
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    df['Time'] = pd.to_datetime(df['Time'])
    df = df[(df['Time'] >= start_date) & (df['Time'] <= end_date)]

    # Generate the temperature graph
    fig_temp = px.line(df, x='Time', y='Temperature (C)', title=f'Temperature in {city} ({start_date} to {end_date})')
    graph_temp = fig_temp.to_html(full_html=False)

    # Generate the humidity graph
    fig_humidity = px.line(df, x='Time', y='Relative Humidity (%)', title=f'Humidity in {city} ({start_date} to {end_date})')
    graph_humidity = fig_humidity.to_html(full_html=False)

    # Generate the wind speed graph
    fig_windspeed = px.line(df, x='Time', y='Wind Speed (m/s)', title=f'Wind Speed in {city} ({start_date} to {end_date})')
    graph_windspeed = fig_windspeed.to_html(full_html=False)

    context = {
        'graph_temp': graph_temp,
        'graph_humidity': graph_humidity,
        'graph_windspeed': graph_windspeed,
        'city': city,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'weather_app/weather_graphs.html', context)