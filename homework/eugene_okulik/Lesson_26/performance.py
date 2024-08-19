import requests
from datetime import datetime


start_time = datetime.now()
requests.get('https://jsonplaceholder.typicode.com/posts/1')
end_time = datetime.now()
first_result = end_time - start_time

start_time = datetime.now()
requests.get('https://jsonplaceholder.typicode.com/posts/42')
end_time = datetime.now()
second_result = end_time - start_time


print(first_result, second_result)
