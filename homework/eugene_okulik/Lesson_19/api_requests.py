import requests


def get_all():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    print(response)
    print(response.text)
    print(response.json()[0]['title'])
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


get_all()


def get_one():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json())


def create_publication():
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF",
        "body": "UYkajshdfkajdshfasdf",
        "userId": 1
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 92834756903845739845'
    }

    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    )

    print(response.json())


def update_with_put():
    payload = {
            "title": "LKJHLKJDHLKJDHLKJDF-UPD",
            "body": "UYkajshdfkajdshfasdf-UPD",
            "userId": 1
        }

    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload
    )

    print(response.json())


def update_with_patch():
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF-UPD"
    }

    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=payload
    )

    print(response.json())


def delete_publication():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    print(response.status_code)
    print(response.json())
