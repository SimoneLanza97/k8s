from flask import Flask, render_template, redirect, request , url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 
import subprocess

#Setting variables for db connection
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_PROTOCOL = os.environ.get ('DB_PROTOCOL')

''' The syntax for the DB_URI connection string is :
DB_URI = protocol://username:password@host:port/database'''
DB_URI = f'{DB_PROTOCOL}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

# Create the class for the table task
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(15), default='To Do', nullable=False)

# Check and create the table task and populate it with the first example task 
with app.app_context():
    db.create_all()
    
    TEST = Task.query.filter_by(status='To Do').all()
    if TEST:
        print("La tabella task è stata creata")
    else:    
        task1 = Task(name='Task 1', description='this is an-example task , you can write the specifics of your task here')
        db.session.add(task1)
        db.session.commit()

''' Define the '/' route , basically when a user go to 127.0.0.1:8080/ the application use a function and 
 returns the task's list an the links to other routes'''      
@app.route('/')
def showList():
    todo_tasks = Task.query.filter_by(status='To Do').all()
    in_progress_tasks = Task.query.filter_by(status='In Progress').all()
    done_tasks = Task.query.filter_by(status='Done').all()
    return render_template('./show_list.html', todo_tasks=todo_tasks, in_progress_tasks=in_progress_tasks, done_tasks=done_tasks) 

# define the '/insert' route
@app.route('/insert', methods=['GET', 'POST'])
def insert_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        
        new_task = Task(name=task_name, description=task_description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('showList'))
    return render_template('insert_task.html')

# define the '/advance' route
@app.route('/advance', methods=['GET','POST'])
def advance_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        selected_task = Task.query.filter_by(name=task_name).first()
        if selected_task:
            if selected_task.status == 'To Do':
                selected_task.status = 'In Progress'
            elif selected_task.status == 'In Progress':
                selected_task.status = 'Done'
            db.session.commit()
            return redirect(url_for('showList'))
        else:
           error_message = f"Nessun elemento trovato con il nome '{task_name}'"
           return render_template('error.html', error_message=error_message)
    else:
        return render_template('advance.html')
        
def delete_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_to_delete = Task.query.filter_by(name=task_name).first()

        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect(url_for('showList'))
        else:
            error_message = f"Nessun elemento trovato con il nome '{task_name}'"
            return render_template('error.html', error_message=error_message)
    else:
        return render_template('delete.html')

# start the application and expose on port 8080
if __name__ == '__main__':
    app.run(port=8080,debug=False)