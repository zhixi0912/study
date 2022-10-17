# 学习目录
# 1。flask路由  //用来匹配url
# 2.request对象 //abort函数
# 3。模版
# 4.flask数据库
# 5。表单
# 6.ajax
# 7.管理系统小案例

# 安装flask，pip install flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
