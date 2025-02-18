from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csc330 spring 2025'

# dictionary of cities with their population
cities = {}

from app import routes
