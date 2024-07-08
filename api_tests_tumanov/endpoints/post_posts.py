import requests

headers_template = {
    'Content-Type': 'application/json'
}


class PostPosts:
    def create_pub(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            'https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()