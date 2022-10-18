#路由
from flask import Flask
app = Flask(__name__)

#路由访问类型
# @app.route('/', methods = ['GET', 'POST'], endpoint="root")
# def root():
#     return 'this is root, please input hello or hi'
# @app.route('/hello', methods = ['GET', 'POST'], endpoint="hello")
# def hello():
#     return 'hello world'
# @app.route('/hi', methods= ['GET', 'POST'], endpoint="hi")
# def hi():
#     return 'hi hi'

#string 接收任何不包含斜杠的文本
#int 接收正整数
#float 接收正浮点数 (2.2)
#path 接收包含斜杠的文本
#路由传参 变量规则
@app.route('/user/<float:id>')
def index(id):
    if id == '1':
        return 'python'
    if id == str(2):
        return 'django'
    if int(id) == 3:
        return 'flask'
    return  'hello world'

if __name__ == '__main__':
    app.run()