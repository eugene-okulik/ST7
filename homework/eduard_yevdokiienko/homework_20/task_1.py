import requests


url = 'https://restful-api.dev/'


def create_object_post():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers
    )
    if response.status_code == 200:
        print("Object created successfully!")
        created_object = response.json()
        print(created_object)
        return created_object.get('id')
    else:
        print(f"Failed to create object. Status code: {response.status_code}")
        print(response.text)


def get_object_by_id(object_id):
    response = requests.get(f'{url}/{object_id}')
    if response.status_code == 200:
        print("Object retrieved successfully!")
        print(response.json())
    else:
        print(f"Failed to retrieve object. Status code: {response.status_code}")
        print(response.text)


def update_object_put(object_id):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(
        f'{url}/{object_id}',
        json=payload
    )
    if response.status_code == 200:
        print("Object updated successfully!")
        print(response.json())
    else:
        print(f"Failed to update object. Status code: {response.status_code}")
        print(response.text)


def partially_update_object_patch(object_id):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        f'{url}/{object_id}',
        json=payload
    )
    if response.status_code == 200:
        print("Name updated successfully!")
        print(response.json())
    else:
        print(f"Failed to update object. Status code: {response.status_code}")
        print(response.text)


def delete_object(object_id):
    response = requests.delete(f'{url}/{object_id}')
    if response.status_code == 200:
        print("Deleted successfully!")
        print(response.json())
    else:
        print(f"Failed to delete. Status code: {response.status_code}")
        print(response.text)


object_id = create_object_post()
get_object_by_id(object_id)
update_object_put(object_id)
partially_update_object_patch(object_id)
delete_object(object_id)
