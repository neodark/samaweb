from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

import json
from collections import OrderedDict

#Declared tests
class TestAPITestSamaMembers(TestCase):
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

        self.updated_json_data = {\
                     'first_name':'one',\
                     'last_name':'matrix2',\
                     'birth_date':'2015-07-25',\
                     'sex':1,\
                     'email':'neo.matrix2@gmail.com',\
                     'address':'street 15',\
                     'npa':5678,\
                     'city':'matrixlandupdated',\
                     'phone':'567.123/89',\
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
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
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

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
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


        request3 = self.client.put('/api/samamembers/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data, sort_keys=True))

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
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


        request3 = self.client.delete('/api/samamembers/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestClientCourseType(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()
        self.json_data = {\
                     'name':'cours 1',\
                     'type':1,\
                     'id':1}

        self.updated_json_data = {\
                     'name':'cours 2',\
                     'type':2,\
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
        request = self.client.get('/api/coursetype/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        request3 = self.client.put('/api/coursetype/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        request3 = self.client.delete('/api/coursetype/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)
