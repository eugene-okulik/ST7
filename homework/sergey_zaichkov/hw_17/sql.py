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
        add_student_req = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
        cursor.execute(add_student_req, ('Crocodile', 'Gena'))
        stud_id = cursor.lastrowid
        db.commit()

        # Add books
        add_book_req = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
        cursor.executemany(add_book_req, [('Cheburashka', stud_id), ('Shapoklyak', stud_id)])
        # cursor.execute(add_book_req, ('Shapoklyak', stud_id,))
        db.commit()

        # Add group
        add_group_req = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
        cursor.execute(add_group_req, ('Gruppa Krovi Na Rukave', '1999-12-31', '2000-01-01'))
        group_id = cursor.lastrowid
        db.commit()

        # Add student into the group
        add_stud_in_group_req = "UPDATE students SET group_id = %s WHERE id = %s"
        cursor.execute(add_stud_in_group_req, (group_id, stud_id))
        db.commit()

        # Add subjects
        add_subj_req = "INSERT INTO subjects (title) VALUES (%s)"
        cursor.execute(add_subj_req, ('Play the accordion',))
        subj1_id = cursor.lastrowid
        cursor.execute(add_subj_req, ('Fly a blue helicopter',))
        subj2_id = cursor.lastrowid
        db.commit()

        # Add lessons
        add_lesson_req = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
        lessons = [('lesson1', subj1_id), ('lesson2', subj1_id), ('lesson3', subj2_id), ('lesson4', subj2_id)]
        less_ids = []
        for lesson in lessons:
            cursor.execute(add_lesson_req, lesson)
            less_ids.append(cursor.lastrowid)
        db.commit()
        less1_id, less2_id, less3_id, less4_id = less_ids

        # Add marks
        add_mark_req = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
        cursor.executemany(
            add_mark_req,
            [
                (8, less1_id, stud_id),
                (3, less2_id, stud_id),
                (7, less3_id, stud_id),
                (10, less4_id, stud_id)
            ]
        )
        db.commit()

        # Get student's marks
        get_marks_req = "SELECT value FROM marks WHERE student_id = %s"
        cursor.execute(get_marks_req, (stud_id,))
        marks = cursor.fetchall()
        print(marks)

        # Get student's books
        get_books_req = "SELECT title FROM books WHERE taken_by_student_id = %s"
        cursor.execute(get_books_req, (stud_id,))
        books = cursor.fetchall()
        print(books)

        # Get student's info
        get_stud_info_req = (
            "SELECT "
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
            "WHERE student_id = %s"
        )
        cursor.execute(get_stud_info_req, (stud_id,))
        stud_info = cursor.fetchall()
        pprint.pp(stud_info)

except Error as e:
    print(e)
