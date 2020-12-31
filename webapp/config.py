from datetime import timedelta
import os

SECRET_KEY = '1373142030:AAFYDHmyB9CZv_plwDRBfExk_KW1Fv9XFa9'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False