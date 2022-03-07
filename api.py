from flask import Flask, make_response, redirect
from flask_restful import Api
from resources.index import index
from resources.datos import datos

# Cambio
app = Flask(__name__)
api = Api(app, catch_all_404s=True)

# def user(name):
#     return f'<h1>Hello {name}!</h1>'

# def cookie():
#     response = make_response('<h1> This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

# def google():
#     return redirect('https://www.google.com')

# def datos():
#     return set(get_datos())

api.add_resource(index, '/')
api.add_resource(datos, '/datos')

# app.add_url_rule('/user/<name>', 'user', user)
# app.add_url_rule('/cookie', 'cookie', cookie)
# app.add_url_rule('/google', 'google', google)
# app.add_url_rule('/datos', 'datos', datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)