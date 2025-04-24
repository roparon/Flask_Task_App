from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import User, Task
from app.forms import TaskForm
from app.forms import UserForm, UserForm

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', title='Home Page', users=users)

@app.route('/users', methods=['GET','POST'])
def users():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            user_name=form.user_name.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash(f'{new_user.first_name} was registered successfully!', 'success')
        return redirect(url_for('tasks'))
    return render_template('register.html', title='Register', user_form=form)

@app.route('/tasks')
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            task_name=form.task_name.data,
            task_description=form.task_description.data,
            task_due_date=form.task_due_date.data
        )
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task "{new_task.title}" addeds successfully!', 'success')
        return redirect(url_for('users'))
    return render_template('tasks.html', title='Tasks', task_form=form)