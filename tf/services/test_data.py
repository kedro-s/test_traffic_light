import json

import requests


class TestDataService:
    base_url = 'http://jsonplaceholder.typicode.com/'

    def __send(self, entity):
        return json.loads(requests.get(self.base_url + entity).text)

    def get_users(self):
        return self.__send(entity='users')

    def get_posts(self):
        return self.__send(entity='posts')

