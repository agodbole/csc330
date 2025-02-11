from flask import Flask

import random

app = Flask (__name__)

@app.route('/')
def greeting():
    return("Hello World!")

@app.route('/random')
def rand():
    return str(random.randint(1,10))


@app.route('/sweet_fruit')
def fruit():
    fruit_list = ["apple","banana","mango","pineapple","orange"]
    return fruit_list[random.randint(0,4)]


