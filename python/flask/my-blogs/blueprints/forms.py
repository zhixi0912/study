# pip install flask-wtf
# pip install email_validator
import wtforms
from wtforms.validators import Email, length, EqualTo
from models import UserModel
import redis


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    v_code = wtforms.StringField(validators=[length(min=4, max=4, message="验证码格式错误")])
    user_name = wtforms.StringField(validators=[length(min=4, max=20, message="用户名格式错误")])
    password = wtforms.StringField(validators=[length(min=6, max=20, message="密码格式错误")])
    confirm_pw = wtforms.StringField(validators=[EqualTo("password", message="两次输入的密码不相同")])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")

    # r.get("news1")
    def validate_v_code(self, field):
        captcha = field.data
        redis_email = self.email.data
        redis_captcha = r.get(redis_email)
        if not redis_captcha or redis_captcha != captcha:
            raise wtforms.ValidationError(message="邮箱或验证码错误")

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[length(min=6, max=20, message="密码格式错误")])
    image_captcha = wtforms.StringField(validators=[length(min=6, max=6, message="验证码格式错误")])