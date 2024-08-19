from locust import task, HttpUser
import random


class PublicationUser(HttpUser):
    token: str

    def on_start(self):
        response = self.client.post('/authorize', json={"name": "Bob"}).json()
        self.token = response['token']

    @task(7)
    def get_all_publications(self):
        headers = {"Authorization": self.token}
        self.client.get('/posts', headers=headers)

    @task(1)
    def create_publication(self):
        headers = {"Authorization": self.token}
        payload = {
            "title": "LKJHLKJDHLKJDHLKJDF",
            "body": "UYkajshdfkajdshfasdf",
            "userId": 1
        }

        self.client.post(
            '/posts',
            json=payload,
            headers=headers
        )

    @task(4)
    def get_publication(self):
        headers = {"Authorization": self.token}
        post_id = random.randrange(1, 101)
        self.client.get(f'/posts/{post_id}', headers=headers)
