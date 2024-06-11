import mysql.connector as mysql


with mysql.connect(
    username='st7',
    password='AVNS_re9xEYl4dUPuhui4A0l',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st7'
) as db:

    cursor = db.cursor(dictionary=True)

    def first_select():
        name = input('name:')
        cursor.execute(f"SELECT * FROM students WHERE name = '{name}'")
        data = cursor.fetchall()
        print(data)
        for line in data:
            print(line['name'])


    def get_one():
        cursor.execute("SELECT * FROM students WHERE id = 1")
        data = cursor.fetchone()
        print(data)
        print(data['name'])


    def insert_into():
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('George', 'Washington2')")
        wash2_id = cursor.lastrowid
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('George', 'Washington3')")
        wash3_id = cursor.lastrowid
        cursor.execute("INSERT INTO students (name, second_name) VALUES ('George', 'Washington4')")
        wash4_id = cursor.lastrowid
        db.commit()
        print(wash3_id, wash2_id, wash4_id)


    def incorrect_formatting():
        name = input('login:')
        second_name = input('password:')
        cursor.execute(
            f"SELECT * FROM students WHERE name = '{name}' "
            f"AND second_name = '{second_name}'"
        )
        user = cursor.fetchall()
        if user:
            print('Logged in')
        else:
            print('User does not exist')


    def correct_formatting():
        name = input('login:')
        second_name = input('password:')
        select_request = 'SELECT * FROM students WHERE name = %s AND second_name = %s'
        cursor.execute(select_request, (name, second_name))
        user = cursor.fetchall()
        if user:
            print('Logged in')
        else:
            print('User does not exist')


    def one_param():
        name = 'George'
        select_request = 'select * from students where name = %s'
        cursor.execute(select_request, (name,))


    def insert_many():
        insert_query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
        cursor.executemany(insert_query, [('Tim', 'Bean'), ('Tim', 'Bean2')])
        ids = cursor.lastrowid
        print(ids)
        db.commit()


    def insert_many_with_ids():
        ids = []
        insert_query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
        for param in [('Tim', 'Bean3'), ('Tim', 'Bean4')]:
            cursor.execute(insert_query, param)
            ids.append(cursor.lastrowid)
        print(ids)
        db.commit()


    def big_query():
        query = '''
        SELECT s.name, g.title as gt, b.title as bt
        FROM students s
        RIGHT JOIN `groups` g
        on s.group_id = g.id
        join books b
        on s.id = b.taken_by_student_id
        WHERE s.id = 1
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
