from db_data_create import get_db_connection


def get_student_marks(cursor, stud_id):
    cursor.execute("""
        SELECT m.value AS Marks
        FROM marks m
        WHERE m.student_id = %s
    """, (stud_id,))
    return cursor.fetchall()


def get_student_books(cursor, stud_id):
    cursor.execute("""
        SELECT b.title AS Books
        FROM books b
        WHERE b.taken_by_student_id = %s
    """, (stud_id,))
    return cursor.fetchall()


def get_full_student_info(cursor, stud_id):
    cursor.execute("""
        SELECT CONCAT(s.name, ' ', s.second_name) AS Student,
               b.title AS Book,
               g.title AS `Group`,
               sub.title AS Subject,
               l.title AS Lessons,
               m.value AS Marks
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON l.id = m.lesson_id
        LEFT JOIN subjects sub ON sub.id = l.subject_id
        WHERE s.id = %s
    """, (stud_id,))
    return cursor.fetchall()


def get_student_info(stud_id):
    try:
        with get_db_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                stud_marks = get_student_marks(cursor, stud_id)
                stud_books = get_student_books(cursor, stud_id)
                all_stud_data = get_full_student_info(cursor, stud_id)

        return stud_marks, stud_books, all_stud_data

    except Exception as e:
        print(f"Error retrieving student information: {e}")
        return [], [], []


def print_info(tables, title=""):
    print(title)
    for row in tables:
        print(row)


if __name__ == "__main__":
    student_id = 14
    marks, books, full_info = get_student_info(student_id)

    print_info(marks, "\nMarks of the student:")
    print_info(books, "\nBooks taken by the student:")
    print_info(full_info, "\nFull information about the student:")
