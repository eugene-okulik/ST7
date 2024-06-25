import unittest
import requests


class TestPublicationApi(unittest.TestCase):
    @staticmethod
    def prep_data():
        return 'TEXT'

    def test_get_all(self):
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
        self.prep_data()
        # print(response)
        # print(response.text)
        # print(response.json()[0]['title'])
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()[0]['title'],
            'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
        )

    def setUp(self):
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

        self.publication_id = response.json()['id']
        # self.publication_id = 42
        print(f'Created publication {self.publication_id}')

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.publication_id}')
        print(f'Publication {self.publication_id} deleted')

    def test_update_with_put(self):
        payload = {
            "title": "LKJHLKJDHLKJDHLKJDF-UPD",
            "body": "UYkajshdfkajdshfasdf-UPD",
            "userId": 1
        }

        response = requests.put(
            f'https://jsonplaceholder.typicode.com/posts/{self.publication_id}',
            json=payload
        )

        print(response.json())
        self.assertEqual(response.json()['title'], payload['title'])
