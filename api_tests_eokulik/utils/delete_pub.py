import requests


def del_pub(pub_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pub_id}')
    print(f'Deleted publication {pub_id}')
