from flask import Blueprint ,render_template, flash, redirect, request, url_for

from webapp import db
from webapp.main_app.forms import TodoForm
from webapp.main_app.models import Todo

blurptint = Blueprint('main_app', __name__, url_prefix='/main_app')


@blurptint.route('/')
def index():
    todo_form = TodoForm()
    incomplete = Todo.query.filter_by(Done=False).all()
    complete = Todo.query.filter_by(Done=True).all()
    return render_template('main_app/index.html', incomplete=incomplete, complete=complete, form=todo_form)


@blurptint.route('/add', methods=['POST'])
def add():
    todo_form = TodoForm()
    todo = Todo(text=request.form['task'], Done=False)
    db.session.add(todo)
    db.session.commit()
    
    return redirect(url_for('main_app.index', form=todo_form))

@blurptint.route('/update', methods=['POST'])
def update():
    todo_form = TodoForm()
    ids = []
    print(request.form)
    dict_of_ids = request.form
    for id in dict_of_ids:
        try:
            ids.append(int(id))
        except ValueError:
            pass

    for number in ids:
        todo = Todo.query.filter_by(id=number).first()
        todo.Done = True
        db.session.commit()
            
    return(redirect(url_for('main_app.index', form=todo_form)))
