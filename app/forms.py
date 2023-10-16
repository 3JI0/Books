from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    books = StringField('Name of Book ', validators=[DataRequired()])
    submit = SubmitField('Add Book')


    