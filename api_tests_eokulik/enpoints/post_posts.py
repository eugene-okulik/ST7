import requests
import allure
from api_tests_eokulik.enpoints.base_api import BaseApi

headers_template = {
    'Content-Type': 'application/json',
}


class PostPosts(BaseApi):
    @allure.step('Create publication')
    def create_publication(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()

    @allure.step('Check response title')
    def check_response_title_is_(self, title):
        assert self.response_json['title'] == title
