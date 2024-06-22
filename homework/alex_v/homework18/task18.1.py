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
