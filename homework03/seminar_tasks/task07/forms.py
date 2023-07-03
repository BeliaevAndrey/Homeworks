from flask_wtf import FlaskForm

from wtforms import (
    PasswordField,
    DateField,
    EmailField,
    StringField,
    SelectField,
    BooleanField
)


from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
)

from task07.custom_validator import Contains


class RegForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(8),
                                                     Contains(alles=True)
                                                     ])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    confirm = BooleanField(label='Confirm', validators=[DataRequired()])

