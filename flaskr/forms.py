from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import Form, BooleanField, StringField, validators
from wtforms import StringField, SubmitField


class RegForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    submit = SubmitField("Submit")
