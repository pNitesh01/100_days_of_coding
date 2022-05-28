from numpy import average


student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum_of_heights = 0
no_of_students = 0

for height in student_heights:
    sum_of_heights += height
    no_of_students += 1

avg_of_heights = round(sum_of_heights/no_of_students)

print(avg_of_heights)
