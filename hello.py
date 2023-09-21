
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
    #return '<h1>Bad Request!</h1>', 400


# Traditional Way
# def index():
#     return '<h1>Hello World</h1>'
#
#
# app.add_url_rule('/', 'index',index )

@app.route('/user/<name>')
def user(name):
    return 'Hello {}'.format(name)


@app.route('/setCookie')
def setCookie():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', '45')
    return response


if __name__ == '__main__':
    app.run()
