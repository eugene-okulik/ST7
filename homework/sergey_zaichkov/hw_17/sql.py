from mysql.connector import connect, Error
import pprint

try:
    with connect(
            username='st7',
            password='AVNS_re9xEYl4dUPuhui4A0l',
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            database='st7'
    ) as db:
        cursor = db.cursor(dictionary=True)

        # Add student
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('Crocodile', 'Gena')")
        stud_id = cursor.lastrowid
        db.commit()

        # Add books
        cursor.execute(f"INSERT INTO books (title, taken_by_student_id)"
                       f" VALUES ('Cheburashka', {stud_id}), ('Shapoklyak', {stud_id})")
        db.commit()

        # Add group
        cursor.execute("INSERT INTO `groups` (title, start_date, end_date)"
                       "VALUES ('Gruppa Krovi Na Rukave', '1999-12-31', '2000-01-01')")
        group_id = cursor.lastrowid
        db.commit()

        # Add student into the group
        cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {stud_id}")
        db.commit()

        # Add subjects
        cursor.execute("INSERT INTO subjects (title) VALUES ('Play the accordion')")
        subj1_id = cursor.lastrowid
        cursor.execute("INSERT INTO subjects (title) VALUES ('Fly a blue helicopter')")
        subj2_id = cursor.lastrowid
        db.commit()

        # Add lessons
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson1', {subj1_id})")
        lesson1_id = cursor.lastrowid
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson2', {subj1_id})")
        lesson2_id = cursor.lastrowid
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson3', {subj2_id})")
        lesson3_id = cursor.lastrowid
        cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('lesson4', {subj2_id})")
        lesson4_id = cursor.lastrowid
        db.commit()

        # Add marks
        cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES "
                       f"(8, {lesson1_id}, {stud_id}),"
                       f"(5, {lesson2_id}, {stud_id}),"
                       f"(2, {lesson3_id}, {stud_id}),"
                       f"(10, {lesson4_id}, {stud_id})")
        db.commit()

        # Get student's marks
        cursor.execute(f"SELECT value FROM marks WHERE student_id = {stud_id}")
        marks = cursor.fetchall()
        print(marks)
        # Get student's books
        cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {stud_id}")
        books = cursor.fetchall()
        print(books)

        # Get student's info
        cursor.execute("SELECT "
                       "students.name AS 'Name',"
                       "students.second_name AS 'Surname',"
                       "groups.title AS 'Group',"
                       "subjects.title AS 'Subject',"
                       "lessons.title AS 'Lesson',"
                       "marks.value AS 'Mark',"
                       "books.title AS 'Book' "
                       "FROM marks "
                       "JOIN lessons ON marks.lesson_id = lessons.id "
                       "JOIN students ON marks.student_id = students.id "
                       "JOIN books ON students.id = books.taken_by_student_id "
                       "JOIN `groups` ON students.group_id = groups.id "
                       "JOIN subjects ON lessons.subject_id = subjects.id "
                       f"WHERE student_id = {stud_id}")
        stud_info = cursor.fetchall()
        pprint.pp(stud_info)
except Error as e:
    print(e)
