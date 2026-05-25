from flask import Flask, render_template
from flask_login import LoginManager, current_user

from pythonProject67.todo.routes import task_bp
from pythonProject67.database.engine import db
from pythonProject67.todo.routes import task_bp
from pythonProject67.auth.routes import auth_bp
from pythonProject67.profile.routes import profile_bp
from pythonProject67.database.models.todo import Task
from pythonProject67.database.models.auth import User

app = Flask(__name__)
login_menager = LoginManager

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '773377'

db.init_app(app)
login_menager.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')

@login_menager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@app.route('/')
def main():
    return render_template('index.html', current_user=current_user)

if __name__ == '__main__':
    app.run(debug=True)