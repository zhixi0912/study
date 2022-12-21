from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! hello me!'

@app.route('/login')
def login():  # put application's code here
    return '我这里是登录!'

if __name__ == '__main__':
    app.run()
