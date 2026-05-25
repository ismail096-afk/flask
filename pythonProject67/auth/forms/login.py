from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    password = StringField('Пароль', validators=[DataRequired(), Length(min=3)])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    remember = BooleanField('Запомни меня')
    submit = SubmitField('Войти')
