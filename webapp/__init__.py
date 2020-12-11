from flask import Flask, render_template

from webapp.model import db
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/')
    def index():
        page_title = 'First page'
        text = 'it is working'
        return render_template('index.html', page_title=page_title, text=text)

    @app.route('/login')
    def login():
        title = 'Autorisation'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
        
    return app
    