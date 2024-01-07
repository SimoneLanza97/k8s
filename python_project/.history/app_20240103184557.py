from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 

# setting ENV variables (temporary)

with open('nome_del_file.txt', 'w') as file:
    file.write('''
export DB_USERNAME="root"
export DB_PASSWORD="password"
export DB_HOST="db"
export DB_PORT="5432"
export DB_NAME="db_app1"
export DB_PROTOCOL="postgresql+psycopg2"
''')

#Setting variables for db connection

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_PROTOCOL = os.environ.get ('DB_PROTOCOL')
''' La Sinstassi per la stringa di connessione al db è :
DB_URI = protocol://username:password@host:port/database'''

DB_URI = f'{DB_PROTCOL}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(15), default='To Do', nullable=False)

with app.app_context():
    db.create_all()
    
    task1 = Task(name='Task 1', description='this is an-example task , you can write the specifics of your task here')
    db.session.add(task1)
    db.session.commit()

@app.route('/')
def showList():
    todo_tasks = Task.query.filter_by(status='To Do').all()
    in_progress_tasks = Task.query.filter_by(status='In Progress').all()
    done_tasks = Task.query.filter_by(status='Done').all()

    return render_template('show_list.html', todo_tasks=todo_tasks, in_progress_tasks=in_progress_tasks, done_tasks=done_tasks)

if __name__ == '__main__':
    app.run(port=8080)