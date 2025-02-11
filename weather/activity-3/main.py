
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/red')
def red():
    return render_template('red.html')

@app.route('/hello/<name>')
def green(name):
    return render_template('green.html',template_name=name)


