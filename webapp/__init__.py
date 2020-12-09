from flask import Flask, render_template

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        page_title = 'First page'
        text = 'it is working'
        return render_template('index.html', page_title=page_title, text=text)

    return app
    