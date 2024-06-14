import mysql.connector as mysql
import os
import dotenv
dotenv.load_dotenv()


with mysql.connect(
    username=os.getenv('DB_USER2'),
    password=os.getenv('DB_PASSW2'),
    host=os.getenv('DB_HOST2'),
    port=os.getenv('DB_PORT2'),
    database=os.getenv('DB_NAME2')
) as db:

    cursor = db.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM students WHERE name = 'George'")
    data = cursor.fetchall()
    print(data)
