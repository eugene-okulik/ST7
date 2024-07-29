from locust import task, HttpUser


class MainUser(HttpUser):
    token = 'cWUrbKHZ0qnL5hI'
    meme_id = 1

    @task(4)
    def create_new_token(self):
        headers = {"Content-Type": "application/json"}
        payload = {"name": "dmitrii_k"}
        response = self.client.post('/authorize', headers=headers, json=payload, catch_response=True)
        response_json = response.json()
        self.token = response_json.get('token')

    @task(1)
    def post_update__delete_meme(self):
        headers = {'Content-Type': 'application/json', 'authorization': self.token}
        payload = {
            "text": "Difference",
            "tags": [
                "QA",
                "bugs",
                "dev"
            ],
            "url": "https://global.discourse-cdn.com/business5/uploads/gemsofwar/original/"
                   "3X/0/e/0ec8397b1ea72bfbf205839b913d3ad2a63df70a.jpeg",
            "info": {}
        }
        response = self.client.post('/meme', headers=headers, json=payload, catch_response=True)
        response_json = response.json()
        self.meme_id = response_json.get('id')

        self.client.get(f'/meme/{self.meme_id}', headers=headers)

        payload = {
            "id": self.meme_id,
            "text": "Change",
            "tags": ["Locust"],
            "url": "https://global.discourse-cdn.com/business5/uploads/gemsofwar/original/"
                   "3X/0/e/0ec8397b1ea72bfbf205839b913d3ad2a63df70a.jpeg",
            "info": {"Changing for performance tests": True}
        }
        self.client.put(f'/meme/{self.meme_id}', headers=headers, json=payload)

        self.client.get(f'/meme/{self.meme_id}', headers=headers)

        self.client.delete(f'/meme/{self.meme_id}', headers=headers)

    @task(11)
    def get_all_memes(self):
        headers = {'Content-Type': 'application/json', 'authorization': self.token}
        print(self.token)
        self.client.get('/meme', headers=headers)

    @task(3)
    def get_meme_by_id(self):
        headers = {'Content-Type': 'application/json', 'authorization': self.token}
        print(self.meme_id)
        self.client.get(f'/meme/{self.meme_id}', headers=headers)
