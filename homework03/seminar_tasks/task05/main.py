from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from task05.forms import RegForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Hello, world!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST' and form.validate():
        data = dict(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
            birthdate=form.birthdate.data
        )
        return render_template('confirm_page.html', **data)
    return render_template('register.html', title='Seminar 03, task 05', form=form)


if __name__ == '__main__':
    app.run(debug=True)
