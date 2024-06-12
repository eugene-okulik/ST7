# Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.
# Важно: никакие id не хардкодить! Хардкод - это если вы в коде пишете значение id. Все id нужно сохранять в
# переменные сразу после добавления данных в базу и потом ими пользоваться.
# При получении данных, распечатывайте эти данные.

import mysql.connector as mysql

with mysql.connect(
    username='st7',
    password='AVNS_re9xEYl4dUPuhui4A0l',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st7'
) as db:

    cursor = db.cursor(dictionary=True)

    def create_student():
        global student_id
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('Elon', 'Musk2')")
        student_id = cursor.lastrowid
        db.commit()
        print(student_id)

    def create_books_by_student():
        create_books_request = "INSERT INTO books (title, taken_by_student_id) values ('Teslasas', %s)"
        cursor.execute(create_books_request, (student_id, ))
        book_id = cursor.lastrowid
        db.commit()
        print(book_id)

    def create_group_for_student():
        cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('Auto', '06.38024', '08.20124')")
        group_id = cursor.lastrowid
        set_group_id_request = 'UPDATE students set group_id = %s where id = %s'
        cursor.execute(set_group_id_request, (group_id, student_id))
        db.commit()
        print(group_id)

    def create_subjects():
        global subject_1
        global subject_2
        cursor.execute("INSERT INTO subjects (title) values ('Enginees')")
        subject_1 = cursor.lastrowid
        cursor.execute("INSERT INTO subjects (title) values ('Planes')")
        subject_2 = cursor.lastrowid
        db.commit()

    def create_lessons():
        global ids
        ids = []
        create_lesson_request = 'INSERT INTO lessons (title, subject_id) values (%s, %s)'
        for param in [('Dryving', subject_1), ('Parking', subject_1), ('Doing nothing', subject_2),
                      ('Dancing', subject_2)]:
            cursor.execute(create_lesson_request, param)
            ids.append(cursor.lastrowid)
        print(ids)
        db.commit()

    def set_marks_to_student():
        set_marks_request = 'INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)'
        for param in [(10, ids[0], student_id), (9, ids[1], student_id), (8, ids[2], student_id),
                      (7, ids[3], student_id)]:
            cursor.execute(set_marks_request, param)
        db.commit()

    def get_student_marks():
        get_marks_query = 'SELECT value FROM marks where student_id = %s'
        cursor.execute(get_marks_query, (student_id,))
        marks = cursor.fetchall()
        print(marks)
        for line in marks:
            print(line['value'])

    def get_student_books():
        get_books_query = ("SELECT title FROM books join students on books.taken_by_student_id = students.id "
                           "where students.id = %s")
        cursor.execute(get_books_query, (student_id,))
        books = cursor.fetchall()
        print(books)

    def get_all_about_student():
        get_all_query = '''
        select * from students join books on students.id=books.taken_by_student_id  join `groups`
        on students.group_id = groups.id
        join marks on students.id = marks.student_id join lessons on marks.lesson_id=lessons.id join subjects on
        lessons.subject_id =subjects.id where students.id=%s
        '''
        cursor.execute(get_all_query, (student_id,))
        student_info = cursor.fetchall()
        print(student_info)

    create_student()
    create_books_by_student()
    create_group_for_student()
    create_subjects()
    create_lessons()
    set_marks_to_student()
    get_student_marks()
    get_student_books()
    get_all_about_student()
