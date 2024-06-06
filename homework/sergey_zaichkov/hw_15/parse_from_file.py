import datetime
import os

dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.join(dir_path, 'homework', 'eugene_okulik', 'hw_15', 'data.txt')

with open(file_path) as f:
    data = f.readlines()

date_1, date_2, date_3 = (datetime.datetime.fromisoformat(string.split(' - ')[0][3:]) for string in data)

TASK_1 = f"{date_1} + 1 week = {date_1 + datetime.timedelta(weeks=1)}"
TASK_2 = f"{date_2} is a {date_2.strftime('%A')}"
TASK_3 = f"{date_3} was {(datetime.datetime.now() - date_3).days} days ago"

print(TASK_1)
print(TASK_2)
print(TASK_3)
