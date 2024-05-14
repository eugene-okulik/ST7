students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_join = ", ".join(students)
subjects_join = ", ".join(subjects)

text = f"Students {students_join} study these subjects: {subjects_join}"
print(text)
