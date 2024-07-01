import mysql.connector as mysql

db = mysql.connect(
        username='st7',
        password='AVNS_re9xEYl4dUPuhui4A0l',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st7'
)
cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) values ('Andrey', 'Kovalev')")
student_id = cursor.lastrowid
db.commit()
print(student_id)


create_books_request = "INSERT INTO books (title, taken_by_student_id) values ('Artur King', %s)"
cursor.execute(create_books_request, (student_id,))
book_id = cursor.lastrowid
db.commit()
print(book_id)


cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('Makarevichi', '1337', '1704')")
group_id = cursor.lastrowid
set_group_id_request = 'UPDATE students set group_id = %s where id = %s'
cursor.execute(set_group_id_request, (group_id, student_id))
db.commit()
print(group_id)

cursor.execute("INSERT INTO subjects (title) values ('Dron')")
subject_1 = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) values ('Baron')")
subject_2 = cursor.lastrowid
db.commit()

ids = []
create_lesson_request = 'INSERT INTO lessons (title, subject_id) values (%s, %s)'
lesson_params = [('1337', subject_1), ('True LS', subject_1), ('AL LS', subject_2), ('JONE SINA', subject_2)]

for param in lesson_params:
    cursor.execute(create_lesson_request, param)
    lesson_id = cursor.lastrowid
    if lesson_id:
        ids.append(lesson_id)
    db.commit()

    if len(ids) == 4:
        set_marks_request = 'INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)'
        marks_params = [(1, ids[0], student_id), (3, ids[1], student_id), (3, ids[2], student_id),
                        (5, ids[3], student_id)]

        for params in marks_params:
            cursor.execute(set_marks_request, params)
        db.commit()

    get_marks_query = 'SELECT value FROM marks where student_id = %s'
    cursor.execute(get_marks_query, (student_id,))
    marks = cursor.fetchall()
    print(marks)
    for line in marks:
        print(line['value'])

        get_books_query = ("SELECT title FROM books join students on books.taken_by_student_id = students.id "
                           "where students.id = %s")
        cursor.execute(get_books_query, (student_id,))
        books = cursor.fetchall()
        print(books)

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
