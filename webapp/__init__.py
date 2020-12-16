from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required

from webapp.model import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        page_title = 'First page'
        text = 'it is working'
        return render_template('index.html', page_title=page_title, text=text)
        
    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hi admin'          
        else:
            return 'You are not admin'
            
    return app
    