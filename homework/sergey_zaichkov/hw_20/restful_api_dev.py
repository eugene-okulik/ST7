import requests

BASE_URL = "https://api.restful-api.dev/objects"


def add_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(
        url=BASE_URL,
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"
    response_dict = response.json()
    return response_dict['id']


def get_object_by_id(id):
    response = requests.get(url=f"{BASE_URL}/{id}")

    assert response.status_code == 200, "Status code is not 200"
    response_dict = response.json()
    return response_dict


def change_object_put(id):
    payload = {
        "name": "ASUS BOOK",
        "data": {
            "year": 2020,
            "price": 1500,
            "CPU model": "Intel Core i666",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(
        url=f"{BASE_URL}/{id}",
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"


def change_object_patch(id):
    payload = {
        "name": "ULTRA MEGA SUPER BOOK-PUK"
    }
    response = requests.patch(
        url=f"{BASE_URL}/{id}",
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"


def delete_object(id):
    response = requests.delete(url=f"{BASE_URL}/{id}")

    assert response.status_code == 200, "Status code is not 200"
    print(response.text)


# Create object
obj_id = add_object()
add_object()
# Get created object
print("New Object is")
print(get_object_by_id(obj_id))

# Change the object by PUT
change_object_put(obj_id)

# Get changed object
print("Changed object by PUT is")
print(get_object_by_id(obj_id))

# Change the object by PATCH
change_object_patch(obj_id)

# Get changed object
print("Changed object by PATCH is")
print(get_object_by_id(obj_id))

# Delete the object
delete_object(obj_id)
