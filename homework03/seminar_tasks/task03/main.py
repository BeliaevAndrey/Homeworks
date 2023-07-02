# Создать базу данных для хранения информации о студентах университета.
# * База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# * В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст,
# пол, группа и id факультета.
# * В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# * Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# * Написать функцию-обработчик, которая будет выводить список всех студентов
# с указанием их факультета.
# =================================================
# * Доработаем задача про студентов
# * Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# * База данных должна содержать две таблицы: "Студенты" и "Оценки".
# * В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# * В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# * Необходимо создать связь между таблицами "Студенты" и "Оценки".
# * Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from random import uniform as _uni, choice as _chc
import json

from flask import Flask, render_template

from task03.models import db, Student, Faculty, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_task03.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def read_students_json():
    with open('task03/static/students_refactored.json', 'r', encoding='utf-8') as f_in:
        studs = json.load(f_in)
    return studs


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    students_dict = read_students_json()

    for faculty_num in range(1, 4):
        faculty = Faculty(name=f'faculty - {faculty_num}')
        db.session.add(faculty)

    count = 0
    for student, params in students_dict.items():
        first_name, _, last_name = student.split()
        count += 1
        db.session.add(Student(
            firstname=first_name,
            lastname=last_name,
            age=students_dict[student]['age'],
            gender=students_dict[student]['gender'],
            group=count % 10 + 1,
            faculty_id=count % 3 + 1
        ))
    db.session.commit()

    for student, params in students_dict.items():
        first_name, _, last_name = student.split()
        a_student = Student.query.filter_by(firstname=first_name,
                                            lastname=last_name,
                                            age=params['age']).all()
        for subj, value in params['marks'].items():
            db.session.add(Mark(
                subject=subj,
                average=value,
                student_id=a_student[0].id
            ))
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'seminar03, task-03: index page',
    }
    return render_template('index.html', **context)


@app.route('/students/')
def students():
    all_students = Student.query.all()

    context = {
        'title': 'seminar03, task-03: Students',
        'students': all_students,
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
