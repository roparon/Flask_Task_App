from app import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

def full_name(self):
    return f"{self.first_name} {self.last_name}"

def display_user(self):
    return f"Full Name: {self.full_name}"
class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def display_task(self):
        status = "Completed" if self.completed else "Pending"
        return (
            f"Task ID: {self.task_id}, "
            f"Title: {self.title}, "
            f"Status: {status}, "
            f"Description: {self.description}"
        )
