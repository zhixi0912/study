# 配置数据库信息
SECRET_KEY = "qwerasdfzxcv"

HOSTNAME = "43.139.138.4"
PORT     = "3306"
DATABASE = "stu_oa" # 数据库名
USERNAME = "root"
PASSWORD = "QWERasdf1234"

DB_URI   = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI



# 配置邮件服务器信息
# pip install flask_mail
# 开启邮箱POP3/SMTP服务
# ghsbdeyymjxcbbbi
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = "True"
MAIL_PORT = 465
MAIL_USERNAME = "985840977@qq.com"
MAIL_PASSWORD = "ghsbdeyymjxcbbbi"
MAIL_DEFAULT_SENDER = "985840977@qq.com"



# 配置REDIS信息
# 1，Mac电脑先安装Homebrew 【https://brew.idayer.com/】
#【/bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"】
# 2，使用brew安装redis 【brew install redis】
# 3，启动redis 【redis-server】
# 4，安装python redis模块 【pip install redis】
# 5，使用连接池连接redis

REDIS_PORT = 6379