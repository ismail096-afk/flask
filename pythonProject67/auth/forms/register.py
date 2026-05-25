from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Никнейм', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=3, max=10)])
    confirm_password = PasswordField('Подтвердить пароль', validators=[
        DataRequired(),
        EqualTo('password', message='Пароль не совпадает')
    ])
    submit = SubmitField('Зарегистрироваться')