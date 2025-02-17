from flask import Flask

import random
import json
import requests
import sys

app = Flask (__name__)

@app.route('/')
def greeting():
    return("Hello World!")

@app.route('/<name>')
def greet_name(name):
    return ("Hello " + name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1+num2)

@app.route('/weather/<city>')
def weather(city):
    payload = {'APPID':'<<API KEY>>', 'q':city}
    url = 'https://api.openweathermap.org/data/2.5/weather'

    response = requests.get(url, params=payload)
    if response.status_code == 200:
        print ('success!', file=sys.stdout)
    elif response.status_Code == 404:
        print ('failure!', file=sys.stdout)

    response_json = response.json()
    formatted_response = json.dumps(response_json, indent=2)
    print (formatted_response, file=sys.stdout)

    temp = response_json['main']['temp']

    message = 'Current temperature in {} is {:0.2f} Celsius'

    return message.format(city, temp - 273)


    
        
