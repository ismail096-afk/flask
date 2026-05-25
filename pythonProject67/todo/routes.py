from flask import Blueprint, render_template, request, redirect, url_for
from pythonProject67.database.models.todo import Task
from pythonProject67.database.engine import db

task_bp = Blueprint('tasks', __name__, template_folder='templates')

tasks_db = [
    {'id': 1, 'title': 'Купить хлеб', 'description': 'Пока не закрылся магазин'},
    {'id': 2, 'title': 'Поменять масло',  'description': 'СТО закрывается в 20:00'},
    {'id': 3, 'title': 'Позвонить Мусе',  'description': 'Разговор о новом проекте'},
    {'id': 4, 'title': 'Создать CRUD',  'description': 'Реализовать CRUD для задач'}
]

@task_bp.route('/')
def get_all_tasks():
    tasks = Task.query.all()# Берем все данные с базы данных
    return render_template('all_tasks.html', tasks_db=tasks)


# Статик - стоит
# Демонически - движется
@task_bp.route('/read/<int:id>')
def task_detail(id):
    task_one = Task.query.all()
    return render_template('index.html', task_one=task_one)

@task_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        # tasks_db.append({'id': len(tasks_db) + 1, 'title': title, 'description': description})
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')

@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_tasks(id):
    task_one = Task.query.filter_by(id=id).first()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title:
            task_one.title = title
        if description:
            task_one.description = description
        db.session.commit()
    return render_template('update.html', task_one=task_one)
@task_bp.route('/delate/<int:id>', methods=['POST'])
def delate_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))

