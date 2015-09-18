from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

import json
from collections import OrderedDict

#Declared tests

class TestAPITestClientSamaGroup(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()
        self.json_data = {\
                     'name':'samagroup 1',\
                     'sama_identifier':1,\
                     'samamembers':[],\
                     'id':1}

        self.updated_json_data = {\
                     'name':'samagroup 2',\
                     'sama_identifier':2,\
                     'samamembers':[],\
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
        request = self.client.get('/api/samagroup/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        request3 = self.client.put('/api/samagroup/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data, sort_keys=True))

        request4 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        #request3 = self.client.delete('/api/samagroup/1', self.updated_json_data, format='json')
        request3 = self.client.delete('/api/samagroup/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

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
                     'samagroup':[],\
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
                     'samagroup':[],\
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


        request3 = self.client.delete('/api/samamembers/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestSamaMembersRelatedToSamaGroups(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()
        self.json_data_samagroup = {\
                     'name':'samagroup 1',\
                     'sama_identifier':1,\
                     'samamembers':[],\
                     'id':1}

        self.json_data_samagroup_updated = {\
                     'name':'samagroup 2',\
                     'sama_identifier':2,\
                     'samamembers':[],\
                     'id':1}

        self.updated_json_data_samagroup = {\
                     'name':'samagroup 1',\
                     'sama_identifier':1,\
                     'samamembers':[1],\
                     'id':1}

        self.updated_json_data_samagroup_updated = {\
                     'name':'samagroup 2',\
                     'sama_identifier':2,\
                     'samamembers':[1],\
                     'id':1}

        self.json_data_samamember = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'samagroup':[],\
                     'id':1}

        self.json_data_samamember_updated = {\
                     'first_name':'one',\
                     'last_name':'matrix2',\
                     'birth_date':'2015-07-25',\
                     'sex':1,\
                     'email':'neo.matrix2@gmail.com',\
                     'address':'street 15',\
                     'npa':5678,\
                     'city':'matrixlandupdated',\
                     'phone':'567.123/89',\
                     'samagroup':[],\
                     'id':1}

        self.updated_json_data_samamember = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'samagroup':[1],\
                     'id':1}

        self.updated_json_data_samamember_updated = {\
                     'first_name':'one',\
                     'last_name':'matrix2',\
                     'birth_date':'2015-07-25',\
                     'sex':1,\
                     'email':'neo.matrix2@gmail.com',\
                     'address':'street 15',\
                     'npa':5678,\
                     'city':'matrixlandupdated',\
                     'phone':'567.123/89',\
                     'samagroup':[1],\
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

    def test_post_relation_samamembers_samagroups_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/samamembers/', self.json_data_samamember, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samamember, sort_keys=True))

        request2 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samamember, sort_keys=True))

        request3 = self.client.post('/api/samagroup/', self.updated_json_data_samagroup, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request4 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request5 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

    def test_post_relation_samagroups_samamembers_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data_samagroup, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samagroup, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samagroup, sort_keys=True))

        request3 = self.client.post('/api/samamembers/', self.updated_json_data_samamember, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))


        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request5 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

    def test_put_relation_samamembers_samagroups_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/samamembers/', self.json_data_samamember, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samamember, sort_keys=True))

        request2 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samamember, sort_keys=True))

        request3 = self.client.post('/api/samagroup/', self.updated_json_data_samagroup, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request4 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request5 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request6 = self.client.put('/api/samamembers/1', self.updated_json_data_samamember_updated, format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request6.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samamember_updated), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request6.content), sort_keys=True), json.dumps(self.updated_json_data_samamember_updated, sort_keys=True))

        request7 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember_updated, sort_keys=True))

        request8 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

    def test_put_relation_samagroups_samamembers_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data_samagroup, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samagroup, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samagroup, sort_keys=True))

        request3 = self.client.post('/api/samamembers/', self.updated_json_data_samamember, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request5 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request6 = self.client.put('/api/samagroup/1', self.updated_json_data_samagroup_updated, format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request6.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samagroup_updated), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request6.content), sort_keys=True), json.dumps(self.updated_json_data_samagroup_updated, sort_keys=True))

        request7 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup_updated, sort_keys=True))

        request8 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

    def test_delete_relation_samamembers_samagroups_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/samamembers/', self.json_data_samamember, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samamember, sort_keys=True))

        request2 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samamember, sort_keys=True))

        request3 = self.client.post('/api/samagroup/', self.updated_json_data_samagroup, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request4 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request5 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request6 = self.client.delete('/api/samamembers/1', format='json')
        self.assertEqual(request6.status_code, status.HTTP_204_NO_CONTENT)

        request7 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request7.content)), 0)

        request8 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samagroup, sort_keys=True))

    def test_delete_relation_samagroups_samamembers_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/samagroup/', self.json_data_samagroup, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_samagroup), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_samagroup, sort_keys=True))

        request2 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samagroup, sort_keys=True))

        request3 = self.client.post('/api/samamembers/', self.updated_json_data_samamember, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_samamember), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request4 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samamember, sort_keys=True))

        request5 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request5.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_samagroup, sort_keys=True))

        request6 = self.client.delete('/api/samagroup/1', format='json')
        self.assertEqual(request6.status_code, status.HTTP_204_NO_CONTENT)

        request7 = self.client.get('/api/samagroup/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request7.content)), 0)

        request8 = self.client.get('/api/samamembers/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_samamember, sort_keys=True))

class TestAPITestDate(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.json_data = {\
                     'date':'2014-01-25T19:00:00Z',\
                     'end_time':'22:00:00',\
                     'id':1,\
                     'courses':[]}

        self.updated_json_data = {\
                     'date':'2015-10-30T20:30:00Z',\
                     'end_time':'23:00:00',\
                     'id':1,\
                     'courses':[]}

    def test_simple_test(self):
        """
        Simple test
        """
        self.assertEqual(2,2)

    def test_get_empty_db(self):
        """
        Testing GET on an empty database
        """
        request = self.client.get('/api/date/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/date/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/date/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        request3 = self.client.put('/api/date/1', self.updated_json_data, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.updated_json_data, sort_keys=True))

        request4 = self.client.get('/api/date/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/date/', self.json_data, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data, sort_keys=True))


        request3 = self.client.delete('/api/date/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/date/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestClientCourseType(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()
        self.json_data = {\
                     'name':'cours 1',\
                     'course_identifier':1,\
                     'courses':[],\
                     'id':1}

        self.updated_json_data = {\
                     'name':'cours 2',\
                     'course_identifier':2,\
                     'courses':[],\
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


        request3 = self.client.delete('/api/coursetype/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestCourse(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()

        self.json_data_coursetype = {\
                     'name':'cours 1',\
                     'course_identifier':1,\
                     'courses':[],\
                     'id':1}

        self.updated_json_data_coursetype = {\
                     'name':'cours 2',\
                     'course_identifier':2,\
                     'courses':[],\
                     'id':1}

        self.json_data_course = {\
                     'course_dates':[],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.updated_json_data_course = {\
                     'course_dates':[],\
                     'location':'Rome',\
                     'inscription_counter':1,\
                     'max_inscription_counter':16,\
                     'status':False,\
                     'course_type':1,\
                     'participants':[],\
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
        request = self.client.get('/api/course/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request3 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request5 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request6 = self.client.get('/api/course/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request3 = self.client.put('/api/coursetype/1', self.updated_json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        tmp_json = self.updated_json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(tmp_json), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(tmp_json, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_coursetype, sort_keys=True))

        request7 = self.client.put('/api/course/1', self.updated_json_data_course, format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request7.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request7.content), sort_keys=True), json.dumps(self.updated_json_data_course, sort_keys=True))

        request8 = self.client.get('/api/course/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_course, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request5 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request6 = self.client.get('/api/course/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request7 = self.client.delete('/api/course/1', format='json')
        self.assertEqual(request7.status_code, status.HTTP_204_NO_CONTENT)

        request8 = self.client.get('/api/course/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request8.content)), 0)

        request3 = self.client.delete('/api/coursetype/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestParticipant(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()

        self.json_data_coursetype = {\
                     'name':'cours 1',\
                     'course_identifier':1,\
                     'courses':[],\
                     'id':1}

        self.updated_json_data_coursetype = {\
                     'name':'cours 2',\
                     'course_identifier':2,\
                     'courses':[],\
                     'id':1}

        self.json_data_course = {\
                     'course_dates':[],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.updated_json_data_course = {\
                     'course_dates':[],\
                     'location':'Rome',\
                     'inscription_counter':1,\
                     'max_inscription_counter':16,\
                     'status':False,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.json_data_participant = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course':1,\
                     'last_course_date':'2015-02-11',\
                     'id':1}

        self.updated_json_data_participant = {\
                     'first_name':'one',\
                     'last_name':'matrix2',\
                     'birth_date':'2015-07-25',\
                     'sex':1,\
                     'email':'neo.matrix2@gmail.com',\
                     'address':'street 15',\
                     'npa':5678,\
                     'city':'matrixlandupdated',\
                     'phone':'567.123/89',\
                     'course':1,\
                     'last_course_date':'2015-03-12',\
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
        request = self.client.get('/api/participants/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request3 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request5 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request5 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request6 = self.client.get('/api/course/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request9 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request9.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request9.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request9.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request10 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request10.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request10.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/course/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request3 = self.client.put('/api/coursetype/1', self.updated_json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        tmp_json = self.updated_json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(tmp_json), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(tmp_json, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_coursetype, sort_keys=True))

        request7 = self.client.put('/api/course/1', self.updated_json_data_course, format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)

        tmp_json = self.updated_json_data_course
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json.dumps(request7.data, sort_keys=True), json.dumps(OrderedDict(tmp_json), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request7.content), sort_keys=True), json.dumps(tmp_json, sort_keys=True))

        request8 = self.client.get('/api/course/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request8.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_course, sort_keys=True))

        request11 = self.client.put('/api/participants/1', self.updated_json_data_participant, format='json')
        self.assertEqual(request11.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request11.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request11.content), sort_keys=True), json.dumps(self.updated_json_data_participant, sort_keys=True))

        request12 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request12.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_participant, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request5 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request6 = self.client.get('/api/course/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request9 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request9.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request9.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request9.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request10 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request10.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request10.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request11 = self.client.delete('/api/participants/1', format='json')
        self.assertEqual(request11.status_code, status.HTTP_204_NO_CONTENT)

        request12 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request12.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request12.content)), 0)
        request7 = self.client.delete('/api/course/1', format='json')
        self.assertEqual(request7.status_code, status.HTTP_204_NO_CONTENT)

        request8 = self.client.get('/api/course/', format='json')
        self.assertEqual(request8.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request8.content)), 0)

        request3 = self.client.delete('/api/coursetype/1', format='json')
        self.assertEqual(request3.status_code, status.HTTP_204_NO_CONTENT)

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request4.content)), 0)

class TestAPITestParticipantsRelatedToCoursesRelatedToCourseTypesAndDates(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()

        self.json_data_date = {\
                     'date':'2014-01-25T19:00:00Z',\
                     'end_time':'19:00:00',\
                     'id':1,\
                     'courses':[]}

        self.updated_json_data_date = {\
                     'date':'2015-10-30T20:30:00Z',\
                     'end_time':'22:00:00',\
                     'id':1,\
                     'courses':[]}

        self.json_data_coursetype = {\
                     'name':'cours 1',\
                     'course_identifier':1,\
                     'courses':[],\
                     'id':1}

        self.json_data_coursetype_updated = {\
                     'name':'cours 2',\
                     'course_identifier':2,\
                     'courses':[],\
                     'id':1}

        self.updated_json_data_coursetype = {\
                     'name':'cours 1',\
                     'course_identifier':1,\
                     'courses':[],\
                     'id':1}

        self.updated_json_data_coursetype_updated = {\
                     'name':'cours 2',\
                     'course_identifier':2,\
                     'courses':[],\
                     'id':1}

        self.json_data_course = {\
                     'course_dates':[],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.json_data_course_date = {\
                     'course_dates':[],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.json_data_course_date_participant = {\
                     'course_dates':[],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.json_data_course_date_participant_repost = {\
                     'course_dates':[1],\
                     'location':'Geneva',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'status':True,\
                     'course_type':1,\
                     'participants':[2],\
                     'id':1}

        self.updated_json_data_course_date_participant = {\
                     'course_dates':[],\
                     'location':'Rome',\
                     'inscription_counter':1,\
                     'max_inscription_counter':16,\
                     'status':False,\
                     'course_type':1,\
                     'participants':[],\
                     'id':1}

        self.json_data_participant_nocourse = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course':None,\
                     'last_course_date':'2015-02-11',\
                     'id':1}

        self.json_data_participant = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course':1,\
                     'last_course_date':'2015-02-11',\
                     'id':1}

        self.json_data_participant_repost = {\
                     'first_name':'neo',\
                     'last_name':'matrix',\
                     'birth_date':'2015-01-25',\
                     'sex':2,\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course':1,\
                     'last_course_date':'2015-02-11',\
                     'id':2}

        self.updated_json_data_participant = {\
                     'first_name':'one',\
                     'last_name':'matrix2',\
                     'birth_date':'2015-07-25',\
                     'sex':1,\
                     'email':'neo.matrix2@gmail.com',\
                     'address':'street 15',\
                     'npa':5678,\
                     'city':'matrixlandupdated',\
                     'phone':'567.123/89',\
                     'course':1,\
                     'last_course_date':'2013-03-18',\
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
        request = self.client.get('/api/participants/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_relation_date_coursetype_courses_participants_db(self):
        """
        Testing a POST and GET on a database
        """
        request3 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request3 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request1 = self.client.post('/api/date/', self.json_data_date, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_date), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_date, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_date, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request5 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

    def test_put_relation_date_coursetype_courses_participants_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request1 = self.client.post('/api/date/', self.json_data_date, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_date), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_date, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_date, sort_keys=True))

        request3 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request3 = self.client.post('/api/course/', self.json_data_course, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_course, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        #tmp_json = self.json_data_course
        #tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request5 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request1 = self.client.put('/api/date/1', self.updated_json_data_date, format='json')
        self.assertEqual(request1.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_date), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.updated_json_data_date, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_date, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course, sort_keys=True))

        request3 = self.client.put('/api/coursetype/1', self.updated_json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request4 = self.client.put('/api/course/1', self.updated_json_data_course_date_participant, format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)

        tmp_json = self.updated_json_data_course_date_participant
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json.dumps(request4.data, sort_keys=True), json.dumps(OrderedDict(tmp_json), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request4.content), sort_keys=True), json.dumps(tmp_json, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_course_date_participant, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.updated_json_data_coursetype
        tmp_json['courses'].append(self.updated_json_data_course_date_participant)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request5 = self.client.put('/api/participants/1', self.updated_json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.updated_json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.updated_json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_participant, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.updated_json_data_course_date_participant
        tmp_json['participants'] =  []
        tmp_json['participants'].append(self.updated_json_data_participant)
        self.assertEqual(json_get, json.dumps(self.updated_json_data_course_date_participant, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_coursetype, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.updated_json_data_date, sort_keys=True))

    def test_delete_relation_date_coursetype_courses_participants_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request1 = self.client.post('/api/date/', self.json_data_date, format='json')
        self.assertEqual(request1.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request1.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_date), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request1.content), sort_keys=True), json.dumps(self.json_data_date, sort_keys=True))

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_date, sort_keys=True))

        request3 = self.client.post('/api/coursetype/', self.json_data_coursetype, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_coursetype), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_coursetype, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        request3 = self.client.post('/api/course/', self.json_data_course_date, format='json')
        self.assertEqual(request3.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request3.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_date), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request3.content), sort_keys=True), json.dumps(self.json_data_course_date, sort_keys=True))

        request4 = self.client.get('/api/course/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_date, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.updated_json_data_coursetype
        tmp_json['courses'].append(self.json_data_course)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        request5 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_participant, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course_date_participant
        tmp_json['participants'].append(self.json_data_participant)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        #Delete participant
        request8 = self.client.delete('/api/participants/1', format='json')
        self.assertEqual(request8.status_code, status.HTTP_204_NO_CONTENT)

        request9 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request9.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request9.content)), 0)

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_date, sort_keys=True))

        #Re-post participant
        request5 = self.client.post('/api/participants/', self.json_data_participant, format='json')
        self.assertEqual(request5.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request5.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant_repost), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request5.content), sort_keys=True), json.dumps(self.json_data_participant_repost, sort_keys=True))

        request6 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request6.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request6.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_repost, sort_keys=True))

        request7 = self.client.get('/api/course/', format='json')
        self.assertEqual(request7.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request7.content):
            json_get = json.dumps(key, sort_keys=True)

        tmp_json = self.json_data_course_date_participant
        tmp_json['participants'] = []
        tmp_json['participants'].append(self.json_data_participant_repost)
        self.assertEqual(json_get, json.dumps(tmp_json, sort_keys=True))

        #Delete course automatically deletes all participants
        request10 = self.client.delete('/api/course/1', format='json')
        self.assertEqual(request10.status_code, status.HTTP_204_NO_CONTENT)

        request11 = self.client.get('/api/course/', format='json')
        self.assertEqual(request11.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request11.content)), 0)

        request12 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request12.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request12.content)), 0)

        request2 = self.client.get('/api/date/', format='json')
        self.assertEqual(request2.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request2.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_date, sort_keys=True))

        request4 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request4.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request4.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_coursetype, sort_keys=True))

        #Delete all one by one
        request8 = self.client.delete('/api/participants/1', format='json')
        self.assertEqual(request8.status_code, status.HTTP_404_NOT_FOUND)

        request9 = self.client.get('/api/participants/', format='json')
        self.assertEqual(request9.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request9.content)), 0)

        request10 = self.client.delete('/api/course/1', format='json')
        self.assertEqual(request10.status_code, status.HTTP_404_NOT_FOUND)

        request11 = self.client.get('/api/course/', format='json')
        self.assertEqual(request11.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request11.content)), 0)

        request13 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request13.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request13.content)), 1)

        request12 = self.client.delete('/api/coursetype/1', format='json')
        self.assertEqual(request12.status_code, status.HTTP_204_NO_CONTENT)

        request13 = self.client.get('/api/coursetype/', format='json')
        self.assertEqual(request13.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request13.content)), 0)

        request15 = self.client.get('/api/date/', format='json')
        self.assertEqual(request15.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request15.content)), 1)

        request14 = self.client.delete('/api/date/1', format='json')
        self.assertEqual(request14.status_code, status.HTTP_204_NO_CONTENT)

        request15 = self.client.get('/api/date/', format='json')
        self.assertEqual(request15.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request15.content)), 0)
