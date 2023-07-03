from wtforms.validators import ValidationError
from string import ascii_letters, digits, punctuation


class Contains:
    """
    Dumb simplified translation of class "AnyOf" from wtforms.validators
    """

    def __init__(self,
                 letters: str = False,
                 numeric: bool = False,
                 punct: bool = False,
                 alles: bool = False):
        self.letters = letters
        self.numeric = numeric
        self.punct = punct
        if alles:
            self.letters = self.numeric = self.punct = True

    def __call__(self, form, field):

        missing = ''
        if self.letters and not set(ascii_letters).intersection(field.data):
            missing += ascii_letters
        if self.numeric and not set(digits).intersection(field.data):
            missing += digits
        if self.punct and not set(punctuation).intersection(field.data):
            missing += punctuation
        print('!!!!!!' * 10, missing)
        if not missing:
            return
        self.values_formatter = self.default_values_formatter
        message = field.gettext("Invalid value, must include at least one of: %(values)s .")
        raise ValidationError(message % dict(values=self.values_formatter(missing)))

    @staticmethod
    def default_values_formatter(values):
        return " ".join(str(x) for x in values)

