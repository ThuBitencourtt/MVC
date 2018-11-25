from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField ("username", validators=[DataRequired()])
    password = PasswordField ("passaword", validators=[DataRequired()])
    remember_me = BooleanField ("remember_me")

class CadastroForm(Form):
    name = StringField ("name", validators=[DataRequired()])
    username = StringField ("username", validators=[DataRequired()])
    email = StringField ("email", validators=[DataRequired()])
    password = PasswordField ("password", validators=[DataRequired()])