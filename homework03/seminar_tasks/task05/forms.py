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


__all__ = ['RegForm']


class Contains:
    """
    Dumb simplified translation of class "AnyOf" from wtforms.validators
    """
    from wtforms.validators import ValidationError
    _default = (',./<>?;:[]{}-=_+!#$%^&*()'
                '1234567890')

    def __init__(self, signs: str = _default):
        self.signs = set(signs)

    def __call__(self, form, field):
        if self.signs.intersection(field.data):
            return
        self.values_formatter = self.default_values_formatter
        message = field.gettext("Invalid value, must include one of: %(values)s .")
        raise self.ValidationError(message % dict(values=self.values_formatter(self.signs)))

    @staticmethod
    def default_values_formatter(values):
        return " ".join(str(x) for x in sorted(values))


class RegForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    confirm = BooleanField(label='Confirm', validators=[DataRequired()])

