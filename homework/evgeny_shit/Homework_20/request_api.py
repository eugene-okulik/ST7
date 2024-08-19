import requests

URL = 'https://api.restful-api.dev/objects'


def create_object(url):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating object: {e}")
        return None


def get_object(url, obj_id):
    try:
        response = requests.get(f"{url}/{obj_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting object: {e}")
        return None


def update_object(url, obj_id):
    payload = {
        "name": "Desktop",
        "data": {
            "year": 2002,
            "price": "free",
            "CPU model": "Intel Celeron (Pentium 4) 2.0",
            "Hard disk size": "1.8 GB",
            "color": "silver"
        }
    }
    try:
        response = requests.put(f"{url}/{obj_id}", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating object: {e}")
        return None


def partial_update_object(url, obj_id):
    payload = {
        "name": "(Updated Name)"
    }
    try:
        response = requests.patch(f"{url}/{obj_id}", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error partially updating object: {e}")
        return None


def delete_object(url, obj_id):
    try:
        response = requests.delete(f"{url}/{obj_id}")
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting object: {e}")
        return None


created_object = create_object(URL)
if created_object:
    object_id = created_object.get('id')
    print(f"Created object: {created_object}")

    print(f"Fetched object: {get_object(URL, object_id)}")

    print(f"Updated object: {update_object(URL, object_id)}")

    print(f"Partially updated object: {partial_update_object(URL, object_id)}")

    print(f"Delete status: {delete_object(URL, object_id)}")
