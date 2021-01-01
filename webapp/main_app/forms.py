from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    task = StringField('Ваша задача', validators=[DataRequired()], render_kw={"class":"form-control"})
    add_button = SubmitField('Добавить',  render_kw={"class":"btn btn-primary"})
    success_button = SubmitField('Сделано', render_kw={"class":"btn btn-success"})