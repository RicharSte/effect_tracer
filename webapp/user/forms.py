from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class': 'form-check-input'})