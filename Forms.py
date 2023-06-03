from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, InputRequired

class AddTask(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    duedate = DateField('Enter Due Date',validators=[InputRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    submit = SubmitField('Submit')

class DeleteTask(FlaskForm):
    submit = SubmitField('Confirm')