import requests

headers_template = {
    'Content-Type': 'application/json',
}


class PostItem:
    def create_item(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            url='https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
        self.response.json = self.response.json()

    def check_status_code_is_200(self, code):
        return self.response.status_code == code

    def check_response_title_is_(self, name):
        return self.response.json()['name'] == name
