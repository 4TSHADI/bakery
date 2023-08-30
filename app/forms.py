from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from app.models import Recipe


class EditRecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    group = StringField('Group', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    steps = TextAreaField('Steps', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Changes')
