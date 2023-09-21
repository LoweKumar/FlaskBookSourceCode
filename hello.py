from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# Traditional Way
# def index():
#     return '<h1>Hello World</h1>'
#
#
# app.add_url_rule('/', 'index',index )

@app.route('/user/<name>')
def user(name):
    return 'Hello {}'.format(name)



if __name__ == '__main__':
    app.run()
