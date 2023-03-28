from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class ActorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = StringField(
        'age', validators=[DataRequired()]
    )
    gender = StringField(
        'gender', validators=[DataRequired()]
    )