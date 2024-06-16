import mysql.connector as mysql
import db_creds


with mysql.connect(
    username=db_creds.username,
    password=db_creds.password,
    host=db_creds.host,
    port=db_creds.port,
    database=db_creds.database
) as db:

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students WHERE name = 'George'")
    data = cursor.fetchall()
    print(data)
    for line in data:
        print(line['name'])
