from flask import render_template, redirect, url_for, flash, request
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

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=1
            )
        db.session.add(new_task)
        db.session.commit()
        flash(f'"{new_task.title}" added successfully!', 'success')
        return redirect(url_for('tasks'))
    tasks = Task.query.all()
    return render_template('tasks.html', title='Tasks', task_form=form, tasks=tasks)

@app.route('/user_list', methods=['GET'])
def user_list():
    users = User.query.all()
    return render_template('user_list.html', title='User List', users=users)



@app.route('/toggle_task/<int:task_id>',methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'{task.title} - status updated successfully!','success')
    return redirect(url_for('tasks'))

@app.route('/delete_task/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task "{task.title}" has been deleted successfully!', 'success')
    return redirect(url_for('tasks'))


@app.route('/edith_task/<int:task_id>', methods=["GET", "POST"])
def edith_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()
    if request.method == 'POST':
        task.title = form.title.data