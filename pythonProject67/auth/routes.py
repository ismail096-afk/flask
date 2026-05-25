from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user

from pythonProject67.auth.forms.register import RegistrationForm
from pythonProject67.auth.forms.login import LoginForm

from pythonProject67.database.engine import db
from pythonProject67.database.models.auth import User

auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static')



@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('tasks.gel_all_tasks'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('tasks.get_all_tasks'))
        else:
            print()

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return  redirect(url_for(('auth.login')))

