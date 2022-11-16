from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
"""
使用SQLAlchemy需要先安装pymysql和SQLAlchemy
1：pip install pymysql
2：pip install flask-sqlalchemy
数据库迁移 要使用到flask-migrate
pip install flask-migrate
"""
app = Flask(__name__)

HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "root1234"
DATABASE = "stu_flask" # 数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
"""
ORM模型映射成表的三步骤：
1：flask db init;只需执行一次
2: flask db migrate:识别ORM模型的改变，生成迁移脚本
3: flask db upgrade:运行迁移脚本，同步到数据库中
"""

with app.app_context(): #上下文
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs.fetchone()) #(1,)



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    # 与article表中的author关联
    # acticles = db.relationship("Article", back_populates="author")

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User",backref="acticles")
    # 与user表中的article关联
    # acticles = db.relationship("User", back_populates="article")

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/user/add")
def add_user():
    user = User(username="张三", password="123456")
    db.session.add(user)
    db.session.commit()
    return "用户创建成功!"

@app.route("/user/query")
def query_user():
    # 1,get查询（主键查找）
    # user = User.query.get(1)
    # print(f"{user.id}:{user.username}-{user.password}")
    # 2,filter_by查询
    # 查询结果是一个Query对象：类数组，可以切片
    users = User.query.filter_by(username="张三")
    for user in users:
        print(user.password)
    return "数据查找成功!"

@app.route("/user/update")
def update_user():
    user = User.query.filter_by(username="张三",).first()
    user.password = "222222"
    db.session.commit()
    return "用户修改成功!"

@app.route("/user/delete")
def delete_user():
    user = User.query.filter_by(username="张三",).first()
    db.session.delete(user)
    db.session.commit()
    return "用户删除成功!"

@app.route("/article/add")
def add_article():
    article1 = Article(title="Flask从入门到放弃", content="Flask先入门，再放弃")
    article1.author = User.query.get(2)

    article2 = Article(title="Django从入门到放弃", content="Django先入门，再放弃")
    article2.author = User.query.get(2)

    db.session.add_all([article1, article2])
    db.session.commit()
    return "文章添加成功!"

@app.route("/article/query")
def query_article():
    user = User.query.get(2)
    for acticle in user.acticles:
        print(acticle.title)
    return "文章查询成功！"



if __name__ == '__main__':
    app.run()
