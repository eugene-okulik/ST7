import mysql.connector as mysql


with mysql.connect(
    username='st7',
    password='AVNS_re9xEYl4dUPuhui4A0l',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st7'
) as db:

    cursor = db.cursor(dictionary=True)

    student_name, student_surname = 'Dmitry', 'Kiseljov'
    query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
    data = (student_name, student_surname)
    cursor.execute(query, data)
    student_id_var = cursor.lastrowid

    query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
    cursor.executemany(
        query, [('Информатика для чайников. Издание 2', student_id_var),
                ('Погружение в базы данных. Издание 2', student_id_var),
                ('Гвидо ван Россум. Детство. Отрочество. Юность. Издание 2', student_id_var)]
    )

    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('st7', '01.04.2024', NULL)")
    group_id = cursor.lastrowid

    query = "UPDATE students SET group_id = %s WHERE name = %s AND second_name = %s"
    data = (group_id, student_name, student_surname)
    cursor.execute(query, data)

    query = 'INSERT INTO subjects (title) VALUES (%s)'
    subject_ids = []
    for item in [['Automation testing on Python'], ['Automation testing on Java']]:
        cursor.execute(query, item)
        subject_ids.append(cursor.lastrowid)

    lesson_ids = []
    query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    lessons = ['python basics', 'java basics', 'advanced python', 'advanced java']
    for i in range(4):
        cursor.execute(query, (lessons[i], subject_ids[i % 2]))
        lesson_ids.append(cursor.lastrowid)

    query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
    marks_dict = {'python basics': 5, 'java basics': 3, 'advanced python': 4, 'advanced java': 2}
    for i in range(4):
        cursor.execute(query, [marks_dict[lessons[i]], lesson_ids[i], student_id_var])

    query = "SELECT * FROM marks WHERE student_id = %s"
    cursor.execute(query, (student_id_var, ))
    marks_data = cursor.fetchall()
    print(marks_data)

    query = "SELECT * FROM books WHERE taken_by_student_id = %s"
    cursor.execute(query, (student_id_var, ))
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
    WHERE s.id = %s
    '''
    data = (student_id_var,)
    cursor.execute(query, data)
    full_data = cursor.fetchall()
    print(full_data)

    db.commit()
