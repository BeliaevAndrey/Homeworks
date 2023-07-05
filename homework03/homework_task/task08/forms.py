from flask_wtf import FlaskForm

from wtforms import (
    PasswordField,
    DateField,
    EmailField,
    StringField,
)


from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
)

from task08.custom_validator import Contains


class RegForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(8),
                                                     Contains(alles=True)
                                                     ])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])
    birthdate = DateField('Birthdate', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
