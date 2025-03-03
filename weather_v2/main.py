# first install requests: sudo pip3 install requests
from flask import Flask, render_template
import requests
import sys
import json

app = Flask(__name__)

@app.route('/temperature/<city>')
def temperature(city):
    payload = {'APPID': '*******************', 'q':city}
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(URL, params = payload)
    if response.status_code == 200:
        print('Success!', file = sys.stdout)
    elif response.status_code == 404:
        print('Not found.', file=sys.stdout)

    response_json = response.json()
    formatted_response = json.dumps(response_json, indent = 2)
    print(formatted_response, file=sys.stdout)

    temperature = response_json['main']['temp']
    s = '<h> Current temperature in {} is {:0.2f} Celsius. </s>'
    return s.format(city, temperature - 273)


def read_temps():
    city_temps = {}
    cities = ['San Diego', 'New York', 'Miami', 'Las Vegas', 'Chicago',
              'Charleston', 'Bozeman', 'Seattle', 'Denver']
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    for city in cities:
        payload = {'APPID': '*******************', 'q':city}
        response = requests.get(URL, params = payload)
        if response.status_code == 200:
            print('Success!', file = sys.stdout)
        elif response.status_code == 404:
            print('Not found.', file=sys.stdout)
        response_json = response.json()
        temperature = response_json['main']['temp']
        city_temps[city] = (int((temperature - 273) * 1.8 + 32))
    return city_temps

@app.route('/show_temps')
def show_temps():
    city_temps = read_temps()
    return render_template('show_temps.html', city_temps = city_temps)


@app.route('/plot_temps')
def plot_temps():
    city_temps = read_temps()
    cities = list(city_temps.keys())
    temps = list(city_temps.values())
    print(cities, file=sys.stdout)
    print(temps, file=sys.stdout)
    return render_template('plot_temps.html',
                            cities = cities,
                            temps = temps)
