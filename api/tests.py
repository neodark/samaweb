from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

import json
from collections import OrderedDict

#Declared tests
class TestAPITestClient(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()
        self.json_data = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'id':1}

    def test_simple_test(self):
        """
        Simple test
        """
        self.assertEqual(2,2)

    def test_get_empty_db(self):
        """
        Testing GET on an empty database
        """
        request = self.client.get('/api/samamembers/', {}, format='json')

    def test_get_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/samamembers/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))
