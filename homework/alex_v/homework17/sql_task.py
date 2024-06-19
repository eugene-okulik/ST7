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
        book_id = cursor.lastrowid
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

