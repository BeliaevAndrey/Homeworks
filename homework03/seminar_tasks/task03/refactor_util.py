import json
from random import randint as rint
from copy import deepcopy

with open('static/students.json', 'r', encoding='utf-8') as f_in:
    students = json.load(f_in)


gender = ['male', 'female']
students_refactored = deepcopy(students)

for key, val in students.items():
    students_refactored[key]['gender'] = gender[key.endswith('а')]
    students_refactored[key]['age'] = rint(18, 50)
    for subj, marks in val['marks'].items():
        students_refactored[key]['marks'][subj] = round(sum(marks) / len(marks), 2)
    students_refactored[key].pop('tests')

# for key, val in students_refactored.items():
#     if val['gender'] == 'female':
#         print(key)
#         for subj, marks in val['marks'].items():
#             print(f'\t{subj}: mean {marks}')
#
# print('=' * 120)
#
# for key, val in students_refactored.items():
#     if val['gender'] == 'male':
#         print(key)
#         for subj, marks in val['marks'].items():
#             print(f'\t{subj}: mean {marks}')


with open('static/students_refactored.json', 'w', encoding='utf-8') as f_out:
    json.dump(students_refactored, f_out, indent=4, ensure_ascii=False)
