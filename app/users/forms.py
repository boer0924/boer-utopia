from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo

class LoginForm(Form):
    username = StringField('openid', [Required('Username is required!')])
    password = PasswordField('password', [Required('Password is required!')])
    remember_me = BooleanField('rememberme', default=False)

class RegisterForm(Form):
    username = StringField('username', [Required(), Length(min=4, max=64)])
    email = StringField('email', [Email()])
    password = PasswordField('password', [Required(), EqualTo('confirm',
        message='Passwords must match')])
    confirm = PasswordField('confirm_password')
