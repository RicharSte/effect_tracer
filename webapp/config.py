from datetime import timedelta
import os

SECRET_KEY = ''

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

REMEMBER_COOKIE_DURATION = timedelta(days=5)