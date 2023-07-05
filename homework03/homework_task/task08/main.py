from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash

from task08.forms import RegForm, LoginForm
from task08.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task08_users.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Hello, world!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


def add_user(user_data: dict[str, str]):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST' and form.validate():
        user_data = dict(
            first_name=form.firstname.data,
            last_name=form.lastname.data,
            email=form.email.data,
            birth_date=form.birthdate.data,
            password=generate_password_hash(form.password.data),
        )
        flash("You've just successfully registered!", 'success')
        add_user(user_data)
    return render_template('register.html', title='Seminar 03, task 07', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user_data = dict(
            email=form.email.data,
            password=form.password.data,
        )
        a_user = User.query.filter_by(email=user_data['email']).all()[0]
        if not a_user:
            flash('User not found in base', 'danger')
            return render_template('login.html', title='Seminar 03, task 07', form=form)
        if check_password_hash(a_user.password, user_data.get('password')):
            flash('You have successfully logged in!', 'success')
        else:
            flash('Wrong password!', 'danger')
            return render_template('login.html', title='Seminar 03, task 07', form=form)
    return render_template('login.html', title='Seminar 03, task 07', form=form)


if __name__ == '__main__':
    app.run(debug=True)
