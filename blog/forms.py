from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Email,EqualTo,Length

"""
Flaskform: a module with already made form"""


class Registrarionform(FlaskForm):
    """a registration class to make html forms easy
    @username: a placeholder for the input field username
    """
    username = StringField('Username',validators=[DataRequired(), Length(min=3,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('signup')


class Loginform(FlaskForm):
    """
    """
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')