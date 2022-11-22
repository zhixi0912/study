from io import BytesIO
from flask import Blueprint, render_template, jsonify, redirect, url_for, session, make_response, flash
from exts import mail, db
from flask_mail import Message
from flask import request
import random
import string
import redis
from .forms import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash # flask加密工具
import VerificationCode

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在系统中不存在")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                if request.form.get('image_captcha').upper() == session.get('veryficationCode').upper():
                    # flash('验证码输入正确')
                    print('验证码输入正确')
                    session["user_id"] = user.id
                    return redirect(url_for("qa.index"))
                else:
                    # flash('验证码输入错误')
                    print('验证码输入错误')
                    return redirect(url_for("auth.login"))
            else:
                print("密码错误")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.user_name.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

@bp.route("/captcha/image")
def captcha():
    # 调用VerificationCode文件中的creatVerificationCode函数生成验证码，并用第1个参数接收图片，第2个参数接收字符
    image_code, char_code = VerificationCode.creatVerificationCode(6)
    # 生成local_buffer对象，以实现在内存中读写bytes
    buffer = BytesIO()
    # 将验证码图片以jpeg格式保存到内存中
    image_code.save(buffer, 'jpeg')
    # 定义一个名为response的响应,内容是内存中的图片文件
    response = make_response(buffer.getvalue())
    # 为响应定义头部关键字段,表明为图片
    response.headers['Content-Type'] = 'image/gif'
    # 验证码字符串存储在seesion中,以供校验输入是否正确
    session['veryficationCode'] = char_code
    # 返回生成的response响应对象,即验证码图片
    return response

@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # print(captcha)
    message = Message(subject="问答博客注册验证码", recipients=[email], body=f"您的验证码是：{captcha}")
    mail.send(message)
    r.set(email, captcha, ex=120)
    print(r.get(email))
    return jsonify({"code": 200, "message": "邮箱验证码发送成功！", "data": None})

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["****@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功！"