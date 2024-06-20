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
        cursor.execute("INSERT INTO students (name,second_name, group_id) Values('Johny','Silverhand', Null)")
        student_id = cursor.lastrowid
        db.commit()

    def create_and_assign_books_to_students():
        create_books = "INSERT INTO books (title, taken_by_student_id) Values ('Green light', %s)"
        cursor.execute(create_books, (student_id,))
        db.commit()

    def create_students_group():
        cursor.execute(
            "insert into `groups` (title, start_date, end_date) values ('Abuse group', 'aug 2024', 'dec 2025')")
        group_id = cursor.lastrowid
        set_group_id = "UPDATE students set group_id = %s where id = %s"
        cursor.execute(set_group_id, (group_id, student_id))
        db.commit()

    def create_subjects():
        global subject1
        global subject2
        cursor.execute("INSERT INTO subjects (title) values ('Abusing A - level')")
        subject1 = cursor.lastrowid
        cursor.execute("INSERT INTO subjects (title) values ('Abusing Pro - level')")
        subject2 = cursor.lastrowid
        db.commit()

    def create_lessons():
        global ids
        ids = []
        create_lessons = "INSERT INTO lessons (title, subject_id) values (%s,%s)"

        for lesson in [('Theory of economics', subject1),
                       ('Macro ecnomics', subject1),
                       ('Reading', subject2),
                       'Writing', subject2]:
            cursor.execute(create_lessons, lesson)
        db.commit()

    def set_marks():
        set_marks = 'INSERT INTO marks (value, lesson_id,student_id) values (%s,%s,%s)'

        for marks in [(7, ids[0], student_id),
                      (8, ids[1], student_id),
                      (7, ids[2], student_id),
                      (2, ids[3], student_id)]:
            cursor.execute(set_marks, marks)
            db.commit()

    def get_student_marks():
        get_marks = 'SELECT value from marks where student_id = %s'
        cursor.execute(get_marks, (student_id,))
        marks = cursor.fetchall()
        for m in marks:
            print(m['value'])

    def get_student_books():
        get_books = (
            "SELECT title FROM books join students on books.taken_by_student_id = students.id "
            "where students.id = %s")

        cursor.execute(get_books, (student_id,))
        cursor.fetchall()

    def get_full_info_about_student():
        get_all = '''
        select * from students join books on students.id= books.taken_by_student_id
        join 'groups' on students.group_id = group.id
        join marks on students.id = marks.student_id join lessons
        on marks.lesson_id = lessons.id join subjects on lessons.subjects.id where.id=%s
        '''
        cursor.execute(get_all, (student_id,))
        cursor.fetchall()

create_subjects()
create_and_assign_books_to_students()
create_students_group()
create_subjects()
create_lessons()
set_marks()
get_student_marks()
get_student_books()
get_full_info_about_student()
