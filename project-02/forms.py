"""
pip install flask - WTF for WT forms
writing Python classes that will be representative of our forms
And then they will automatically be converted in the HTML forms within our
template
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

"""
we wanted to create a registration form then we can create a registration form
class. And this will inherit from flask form.
Now within our form we're going to have different form fields and these form
fields are all going to be imported classes as well.

imported from wtf packages not flask packages
'Username' - Label String Field html
validators - does vaidation (string cant empty and 2-50 char long string)
"""


class RegistrationForm(FlaskForm):
    # few limitations that we want to put in place
    # So first of all we want to make sure they actually put something for
    # their username and just don't leave it empty or blank
    # we wouldn't want a user to be able to create a username 2-20 char long
    # Validators are also going to be classes that we import so to make sure
    # a field isn't empty

    # DataRequired : says can't be empty fields
    # Length 2-20 char long
    name_of_student = StringField(
                'Name of student',
                validators=[DataRequired(), Length(min=2, max=20)]
    )

    roll_number = IntegerField(
        'Roll Number',
        validators=[DataRequired(), Length(min=10, max=12)]
    )

    batch_name = StringField(
            'Batch Name',
            validators=[DataRequired(), Length(min=5, max=20)]
    )

    fathers_name = StringField(
            'Fathers Name',
            validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField(
                'Email',
                validators=[DataRequired(), Email()]
    )

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField(
                    'confirm_password',
                    validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign up')
