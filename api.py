from distutils.log import debug
from flask import Flask, make_response, redirect

# Cambio
app = Flask(__name__)

def index():
    return '<h1>Hello World!</h1>'

def user(name):
    return f'<h1>Hello {name}!</h1>'

def cookie():
    response = make_response('<h1> This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

def google():
    return redirect('https://www.google.com')

app.add_url_rule('/', 'index', index)
app.add_url_rule('/user/<name>', 'user', user)
app.add_url_rule('/cookie', 'cookie', cookie)
app.add_url_rule('/google', 'google', google)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)