from flask import render_template, redirect, url_for, flash, request
import sqlalchemy
from app import app, db
from app.models import User, Task
from app.forms import TaskForm
from app.forms import UserForm, UserForm, LoginForm
from flask_login import login_user, login_required, logout_user, current_user

@app.route('/')
def home():
    return render_template('index.html', title='Home Page', users=users)

@app.route('/users', methods=['GET', 'POST'])
def users():
    form = UserForm()
    if form.validate_on_submit():
        try:
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
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            flash('Username already exists. Please choose a different one.', 'danger')
    return render_template('register.html', title='Register', user_form=form)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            new_task = Task(
                title=form.title.data,
                description=form.description.data,
                completed=form.completed.data,
                user_id=current_user.user_id  # <-- Use current_user.user_id
            )
            db.session.add(new_task)
            db.session.commit()
            flash(f'"{new_task.title}" added successfully!', 'success')
            return redirect(url_for('tasks'))
    
    if current_user.is_authenticated:
        tasks = Task.query.filter_by(user_id=current_user.user_id).all()  # <-- Use current_user.user_id
    else:
        flash("Please log in to view your tasks.", "warning")
        return redirect(url_for('login'))
    
    return render_template('tasks.html', tasks=tasks, form=form)


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
    if request.method == 'POST' and form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.completed = form.completed.data
        db.session.commit()
        flash(f'Task "{task.title}" has been updated successfully!', 'success')
        return redirect(url_for('tasks'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.completed.data = task.completed
        tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', title='Edith Tasks', task_form=form, tasks=tasks, edith_mode=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(user_name=form.username.data).first()
            if user and user.password == form.password.data:
                flash(f'Welcome back, {user.first_name}!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Failed to log in. Try again.', 'danger')
    return render_template('login.html', title='Login', login_form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfully!', 'success')
    return redirect(url_for('login')) 