import mysql.connector as mysql

with mysql.connect(
        username='st7',
        password='AVNS_re9xEYl4dUPuhui4A0l',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st7'
) as db:

    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Eduard', 'Yevdokiienko', NULL)")
    eduard_id = cursor.lastrowid
    eduard_data = cursor.fetchall()

    insert_book_1 = '''INSERT INTO books (title, taken_by_student_id) VALUES ('3 body problem', %s)'''
    cursor.execute(insert_book_1, (eduard_id,))
    book_1_id = cursor.lastrowid
    insert_book_2 = '''INSERT INTO books (title, taken_by_student_id) VALUES ('S_Q_L', %s)'''
    cursor.execute(insert_book_2, (eduard_id,))
    book_2_id = cursor.lastrowid
    books_data = cursor.fetchall()

    insert_group = '''INSERT INTO `groups` (title, start_date, end_date) VALUES ('ST777', '2024-04-04', '2024-08-01')'''
    cursor.execute(insert_group)
    my_group_id = cursor.lastrowid
    put_student_into = '''UPDATE students SET group_id =%s WHERE id =%s'''
    cursor.execute(put_student_into, (my_group_id, eduard_id))
    group_data = cursor.fetchall()

    insert_subject_1 = '''INSERT INTO subjects (title) VALUES ('Math')'''
    cursor.execute(insert_subject_1)
    subject_1_id = cursor.lastrowid
    insert_subject_2 = '''INSERT INTO subjects (title) VALUES ('Sciense')'''
    cursor.execute(insert_subject_2)
    subject_2_id = cursor.lastrowid
    subject_data = cursor.fetchall()

    insert_lesson_1 = '''INSERT INTO lessons (title, subject_id) VALUES ('Theory of mathematics', %s)'''
    cursor.execute(insert_lesson_1, (subject_1_id,))
    lesson_1_id = cursor.lastrowid
    insert_lesson_2 = '''INSERT INTO lessons (title, subject_id) VALUES ('Practice of Math', %s)'''
    cursor.execute(insert_lesson_2, (subject_1_id,))
    lesson_2_id = cursor.lastrowid
    insert_lesson_3 = '''INSERT INTO lessons (title, subject_id) VALUES ('Theory of Science', %s)'''
    cursor.execute(insert_lesson_3, (subject_2_id,))
    lesson_3_id = cursor.lastrowid
    insert_lesson_4 = '''INSERT INTO lessons (title, subject_id) VALUES ('Practice of Science', %s)'''
    cursor.execute(insert_lesson_4, (subject_2_id,))
    lesson_4_id = cursor.lastrowid
    lesson_data = cursor.fetchall()

    insert_mark_1 = '''INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', %s, %s)'''
    cursor.execute(insert_mark_1, (lesson_1_id, eduard_id))
    mark_1_id = cursor.lastrowid
    insert_mark_2 = '''INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', %s, %s)'''
    cursor.execute(insert_mark_2, (lesson_2_id, eduard_id))
    mark_2_id = cursor.lastrowid
    insert_mark_3 = '''INSERT INTO marks (value, lesson_id, student_id) VALUES ('A', %s, %s)'''
    cursor.execute(insert_mark_3, (lesson_3_id, eduard_id))
    mark_3_id = cursor.lastrowid
    insert_mark_4 = '''INSERT INTO marks (value, lesson_id, student_id) VALUES ('B', %s, %s)'''
    cursor.execute(insert_mark_4, (lesson_4_id, eduard_id))
    mark_4_id = cursor.lastrowid
    marks_data = cursor.fetchall()

    db.commit()

    query_eduard_marks = f'''SELECT * FROM marks WHERE student_id = %s'''
    cursor.execute(query_eduard_marks, (eduard_id,))
    eduard_marks = cursor.fetchall()
    print(eduard_marks)

    query_eduard_books = f'''SELECT * FROM books b  WHERE taken_by_student_id =%s'''
    cursor.execute(query_eduard_books, (eduard_id,))
    eduard_books = cursor.fetchall()
    print(eduard_books)

    query_general = f'''SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title, m.value AS mark,
                    l.title AS lesson_title, sub.title AS subject_title
                    FROM students s
                    JOIN `groups` g ON g.id = s.group_id
                    JOIN books b ON b.taken_by_student_id = s.id
                    JOIN marks m ON m.student_id = s.id
                    JOIN lessons l ON l.id = m.lesson_id
                    JOIN subjects sub ON sub.id = l.subject_id
                    WHERE s.id = %s'''
    cursor.execute(query_general, (eduard_id,))
    eduard_info = cursor.fetchall()
    print(eduard_info)

db.close()
