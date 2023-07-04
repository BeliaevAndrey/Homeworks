from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.id}, {self.name})'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return (f'Student('
                f'{self.id}, '
                f'{self.firstname}, '
                f'{self.lastname}, '
                f'{self.age}, '
                f'{self.gender}, '
                f'{self.group}, '
                f'{self.faculty_id}'
                f')')


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    average = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    students = db.relationship('Student', backref='marks')

    def __repr__(self):
        return f'Mark({self.subject} {self.average})'

    def get_subj(self):
        return f'{self.subject}'

    def get_average(self):
        return f'{self.average}'
