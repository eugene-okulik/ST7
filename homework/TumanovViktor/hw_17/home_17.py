import mysql.connector as mysql

# Connect to the MySQL database
with mysql.connect(
        username='st7',
        password='AVNS_re9xEYl4dUPuhui4A0l',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st7'
) as db:
    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
                   ('Viktor', 'Tumanov', 6))
    db.commit()

    student_id = cursor.lastrowid

    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   ('Dora', student_id))
    db.commit()
    book1_id = cursor.lastrowid

    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   ('DodoBook', student_id))
    db.commit()
    book2_id = cursor.lastrowid

    cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
                   ('Dorado', student_id))
    db.commit()
    book3_id = cursor.lastrowid

    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('SQL',))
    db.commit()
    subject1_id = cursor.lastrowid

    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('MySQL',))
    db.commit()
    subject2_id = cursor.lastrowid

    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   ('sleep 9-12', subject1_id))
    db.commit()
    lesson1_id = cursor.lastrowid

    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   ('sleep 12-3', subject1_id))
    db.commit()
    lesson2_id = cursor.lastrowid

    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   ('Magic lessons 21:00', subject2_id))
    db.commit()
    lesson3_id = cursor.lastrowid

    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   ('Magic lessons 00:00', subject2_id))
    db.commit()
    lesson4_id = cursor.lastrowid

    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (5, lesson1_id, student_id))
    db.commit()
    mark1_id = cursor.lastrowid

    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (5, lesson2_id, student_id))
    db.commit()
    mark2_id = cursor.lastrowid

    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (4, lesson3_id, student_id))
    db.commit()
    mark3_id = cursor.lastrowid

    cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   (2, lesson4_id, student_id))
    db.commit()
    mark4_id = cursor.lastrowid

    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
                   ('Nara', 'start 2024', 'End 2025'))
    db.commit()
    group_id = cursor.lastrowid

    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    print(cursor.fetchone())

    cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM subjects")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM lessons")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
    print(cursor.fetchone())

    cursor.execute("""
            SELECT students.name, students.second_name, `groups`.title AS group_name, books.title AS book_title,
             marks.value, lessons.title AS lesson_title, subjects.title AS subject_title
            FROM students
            LEFT JOIN `groups` ON students.group_id = `groups`.id
            LEFT JOIN books ON students.id = books.taken_by_student_id
            LEFT JOIN marks ON students.id = marks.student_id
            LEFT JOIN lessons ON marks.lesson_id = lessons.id
            LEFT JOIN subjects ON lessons.subject_id = subjects.id
            WHERE students.name = 'Viktor' AND students.second_name = 'Tumanov'
        """)

    student_info = cursor.fetchall()
    print(student_info)
