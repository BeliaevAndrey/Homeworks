from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect

# from forms import RegForm
from task07.forms import RegForm

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
        flash("You've just successfully registered!", 'success')
    return render_template('register.html', title='Seminar 03, task 07', form=form)


if __name__ == '__main__':
    app.run(debug=True)
