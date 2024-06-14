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
        cursor.execute("INSERT INTO students (name, second_name) values ('Tuman', 'Vitya')")
        student_id = cursor.lastrowid
        db.commit()
        print(student_id)

    def create_books_by_student():
        create_books_request = "INSERT INTO books (title, taken_by_student_id) values ('Dodo', %s)"
        cursor.execute(create_books_request, (student_id, ))
        book_id = cursor.lastrowid
        db.commit()
        print(book_id)

    def create_group_for_student():
        cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('Pushkin', '2024', '2025')")
        group_id = cursor.lastrowid
        set_group_id_request = 'UPDATE students set group_id = %s where id = %s'
        cursor.execute(set_group_id_request, (group_id, student_id))
        db.commit()
        print(group_id)

    def create_subjects():
        global subject_1
        global subject_2
        cursor.execute("INSERT INTO subjects (title) values ('sql')")
        subject_1 = cursor.lastrowid
        cursor.execute("INSERT INTO subjects (title) values ('mysql')")
        subject_2 = cursor.lastrowid
        db.commit()

    def create_lessons():
        global ids
        ids = []
        create_lesson_request = 'INSERT INTO lessons (title, subject_id) values (%s, %s)'
        for param in [('sleep 21-00', subject_1), ('sleep 23-00', subject_1), ('sleep 00-06', subject_2),
                      ('sleep 06-12', subject_2)]:
            cursor.execute(create_lesson_request, param)
            ids.append(cursor.lastrowid)
        print(ids)
        db.commit()

    def set_marks_to_student():
        set_marks_request = 'INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)'
        for param in [(7, ids[0], student_id), (5, ids[1], student_id), (2, ids[2], student_id),
                      (1, ids[3], student_id)]:
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
        select * from students
        join books 
        on students.id=books.taken_by_student_id
        join `groups`
        on students.group_id = groups.id
        join marks
        on students.id = marks.student_id
        join lessons
        on marks.lesson_id=lessons.id
        join subjects
        on
        lessons.subject_id =subjects.id
        where students.id=%s
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
