import requests
import allure
from test_api_dmitrii.endpoints.base_api import BaseApi
from test_api_dmitrii.tests.data import url


class GetPosts(BaseApi):
    @allure.step('Get all Posts')
    def get_posts(self):

        self.response = requests.get(
            url.url
        )
