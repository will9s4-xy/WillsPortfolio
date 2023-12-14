from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='to do', nullable=False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task_content = request.form.get('task')
    new_task_status = request.form.get('status')
    if new_task_content and new_task_status:
        new_task = Task(content=new_task_content, status=new_task_status)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    task_to_edit = Task.query.get(task_id)
    if task_to_edit:
        new_content = request.form.get('editContent')
        new_status = request.form.get('editStatus')

        if new_content:
            task_to_edit.content = new_content
        if new_status:
            task_to_edit.status = new_status

        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
