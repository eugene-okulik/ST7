
import mysql.connector as mysql
import os
import dotenv
dotenv.load_dotenv()


with mysql.connect(
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
) as db:

    cursor = db.cursor(dictionary=True)

    cursor.execute("INSERT INTO students (name, second_name) VALUES ('Kate', 'Shargaeva')")
    new_st = cursor.lastrowid

    cursor.execute("insert into books (title) values ('Cinderella')")
    new_book_1 = cursor.lastrowid

    cursor.execute("insert into books (title) values ('The Pig')")
    new_book_2 = cursor.lastrowid

    updated_book = 'Update books set taken_by_student_id = %s where id = %s'
    cursor.execute(updated_book, (new_st, new_book_1))

    updated_book = 'Update books set taken_by_student_id = %s where id = %s'
    cursor.execute(updated_book, (new_st, new_book_2))

    cursor.execute("insert into `groups` (title, start_date, end_date) values ('Cubes', 'April 2024', 'July 2024')")
    new_group = cursor.lastrowid

    updated_group = 'Update students set group_id = %s where id = %s'
    cursor.execute(updated_group, (new_group, new_st))

    new_subject1 = 'insert into subjects (title) values (%s)'
    cursor.execute(new_subject1, [('Language Arts'),])
    s1_id = cursor.lastrowid

    new_subject2 = 'insert into subjects (title) values (%s)'
    cursor.execute(new_subject2, [('PLTW'),])
    s2_id = cursor.lastrowid

    les1_ids = []
    new_les_sub1 = 'insert into lessons (title, subject_id) values (%s, %s)'
    for param in [('Reading', s1_id), ('Writing', s1_id)]:
        cursor.execute(new_les_sub1, param)
        les1_ids.append(cursor.lastrowid)

    les2_ids = []
    new_les_sub2 = 'insert into lessons (title, subject_id) values (%s, %s)'
    for param in [('Programming', s2_id), ('Design', s2_id)]:
        cursor.execute(new_les_sub2, param)
        les2_ids.append(cursor.lastrowid)

    marks_sub1 = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
    cursor.executemany(marks_sub1, [(96, les1_ids[0], new_st), (89, les1_ids[1], new_st)])

    marks_sub2 = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
    cursor.executemany(marks_sub2, [(99, les2_ids[0], new_st), (100, les2_ids[1], new_st)])
    db.commit()

    student_marks = ('select value from marks where student_id = %s')
    cursor.execute(student_marks, (new_st,))
    all_marks = cursor.fetchall()
    print(all_marks)

    student_books = ('select title from books where taken_by_student_id = %s')
    cursor.execute(student_books, (new_st,))
    all_books = cursor.fetchall()
    print(all_books)

    all_about_student = '''
    select * from students
    left join books on students.id = taken_by_student_id
    left join marks on students.id = student_id
    left join lessons on marks.lesson_id = lessons.id
    left join subjects on lessons.subject_id = subjects.id
    where students.id = %s
    '''
    cursor.execute(all_about_student, (new_st,))
    final_data = cursor.fetchall()
    print(final_data)
