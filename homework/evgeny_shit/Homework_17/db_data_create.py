from random import randint

import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
        port="25060",
        user="st7",
        password="AVNS_re9xEYl4dUPuhui4A0l",
        database="st7"
    )


if __name__ == "__main__":
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO students (name, second_name) VALUES ('Davy', 'Jones')")
            student_id = cursor.lastrowid

            books = ['A cursed treasure', 'The depths of the Sirens', 'Captain Jack Sparrow']
            for book in books:
                cursor.execute(
                    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", (book, student_id)
                )

            cursor.execute(
                "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Pirates', '2023-01-01', '2024-06-11')"
            )
            group_id = cursor.lastrowid

            cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))

            subjects = {
                'Robbery': ['Capture', 'Threat'],
                'Boarding': ['Oar work', 'Hook throwing'],
                'Shooting': ['Aiming', 'Reloading']
            }
            lesson_ids = []
            for subject, lessons in subjects.items():
                cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
                subject_id = cursor.lastrowid

                for lesson in lessons:
                    cursor.execute(
                        "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson, subject_id)
                    )
                    lesson_ids.append(cursor.lastrowid)

            marks = [(randint(0, 100), lesson_id, student_id) for lesson_id in lesson_ids]
            cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", marks)

        conn.commit()
