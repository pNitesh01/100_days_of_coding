import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_score = {name:random.randint(1, 100) for name in names}

passed_students = {name:score for (name, score) in students_score.items() if score >= 60}

print(students_score)
print(passed_students)