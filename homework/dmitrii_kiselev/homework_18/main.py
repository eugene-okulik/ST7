import mysql.connector as mysql
import dotenv
import os


dotenv.load_dotenv()

with mysql.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
) as db:

    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('st7', '01.04.2024', NULL)")
    group_id = cursor.lastrowid

    cursor.execute(f"INSERT INTO students (name, second_name, group_id) VALUES ('Dmitrii', 'Kiselev', {group_id})")
    student_id_var = cursor.lastrowid

    quary = f'INSERT INTO books (title, taken_by_student_id) VALUES (%s, {student_id_var})'
    cursor.executemany(quary, [['Информатика для чайников'], ['Погружение в базы данных'],
                               ['Гвидо ван Россум. Детство. Отрочество. Юность']])

    quary = 'INSERT INTO subjects (title) VALUES (%s)'
    subject_ids = []
    for item in [['Automation testing on Python'], ['Automation testing on Java']]:
        cursor.execute(quary, item)
        subject_ids.append(cursor.lastrowid)

    lesson_ids = []
    quary = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    lessons = ['SQL', 'SQL + JAVA', 'SQL on python', 'dotenv']
    for i in range(4):
        cursor.execute(quary, (lessons[i], subject_ids[i % 2]))
        lesson_ids.append(cursor.lastrowid)

    quary = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
    marks_dict = {'SQL': 5, 'SQL + JAVA': 3, 'SQL on python': 4, 'dotenv': 5}
    for i in range(4):
        cursor.execute(quary, [marks_dict[lessons[i]], lesson_ids[i], student_id_var])

    cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id_var}")
    marks_data = cursor.fetchall()
    print(marks_data)

    cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id_var}")
    books_data = cursor.fetchall()
    print(books_data)

    query = '''
    SELECT * FROM students s
    JOIN `groups` g
    ON s.group_id = g.id
    JOIN books b
    ON s.id = b.taken_by_student_id
    JOIN marks m
    ON s.id = m.student_id
    JOIN lessons l
    ON m.lesson_id = l.id
    JOIN subjects s2
    ON l.subject_id = s2.id
    WHERE s.id = 80
    '''
    cursor.execute(query)
    full_data = cursor.fetchall()
    print(full_data)

    db.commit()
