from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase

import json
from collections import OrderedDict

#Declared tests

class SamaTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        #COURSE
        #POST
        self.json_data_course_post = {\
                     'status':'O',\
                     'course_type':'B',\
                     'max_inscription_counter':12,\
                     'additional_information':{\
                        'dates':'10-02-2015 10-03-2015',\
                        'location':'Geneva',\
                        'time':'Le cours a lieu de 19h00 a 22h30'}\
                     }

        self.json_data_course_post_api_reply = {\
                     'status_api':'success_creation',\
                     'status':'O',\
                     'course_type':'B',\
                     'max_inscription_counter':12,\
                     'additional_information':"{\"dates\": \"10-02-2015 10-03-2015\", \"location\": \"Geneva\", \"time\": \"Le cours a lieu de 19h00 a 22h30\"}"\
                     }

        self.json_data_course_post_get_verification = {\
                     'id':1,\
                     'status':'open',\
                     'course_type':'samaritains',\
                     'inscription_counter':0,\
                     'max_inscription_counter':12,\
                     'participants':[],\
                     'additional_information':{\
                        'dates':'10-02-2015 10-03-2015',\
                        'location':'Geneva',\
                        'time':'Le cours a lieu de 19h00 a 22h30'}\
                     }

        #PUT
        self.json_data_course_put = {\
                     'status':'C',\
                     'course_type':'D',\
                     'max_inscription_counter':14,\
                     'additional_information':{\
                        'dates':'09-03-2016 07-05-2016',\
                        'location':'Lausanne',\
                        'time':'Le cours a lieu de 15h00 a 16h45'}\
                     }

        self.json_data_course_put_api_reply = {\
                     'status_api':'success_update',\
                     'status':'C',\
                     'course_type':'D',\
                     'max_inscription_counter':14,\
                     'additional_information':"{\"dates\": \"09-03-2016 07-05-2016\", \"location\": \"Lausanne\", \"time\": \"Le cours a lieu de 15h00 a 16h45\"}"\
                     }

        self.json_data_course_put_get_verification = {\
                     'id':1,\
                     'status':'closed',\
                     'course_type':'bls-aed',\
                     'inscription_counter':0,\
                     'max_inscription_counter':14,\
                     'participants':[],\
                     'additional_information':{\
                        'dates':'09-03-2016 07-05-2016',\
                        'location':'Lausanne',\
                        'time':'Le cours a lieu de 15h00 a 16h45'}\
                     }

        #PARTICIPANT
        #POST
        self.json_data_participant_post = {\
                     'status': 'S',\
                     'first_name': 'Neo',\
                     'last_name': 'Matrix',\
                     'birth_date':'2000-01-25',\
                     'gender': 'M',\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course': 1\
                     }

        self.json_data_participant_post_api_reply = {\
                     'status_api':'success_creation',\
                     'status': 'S',\
                     'first_name': 'Neo',\
                     'last_name': 'Matrix',\
                     'birth_date':'2000-01-25',\
                     'gender': 'M',\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course': 1\
                     }

        self.json_data_participant_post_get_verification = {\
                     'id':1,\
                     'status': 'student',\
                     'first_name': 'Neo',\
                     'last_name': 'Matrix',\
                     'birth_date':'2000-01-25',\
                     'gender': 'M',\
                     'email':'neo.matrix@gmail.com',\
                     'address':'street 12',\
                     'npa':1234,\
                     'city':'matrixland',\
                     'phone':'123.145/34',\
                     'course': 1\
                     }

        self.json_data_participant_post_get_course_verification = {\
                     'id':1,\
                     'status':'open',\
                     'course_type':'samaritains',\
                     'inscription_counter':1,\
                     'max_inscription_counter':12,\
                     'participants':[self.json_data_participant_post_get_verification],\
                     'additional_information':{\
                        'dates':'10-02-2015 10-03-2015',\
                        'location':'Geneva',\
                        'time':'Le cours a lieu de 19h00 a 22h30'}\
                     }

        #PUT
        self.json_data_participant_put = {\
                     'status': 'C',\
                     'first_name': 'John',\
                     'last_name': 'Doe',\
                     'birth_date':'2007-07-11',\
                     'gender': 'F',\
                     'email':'john.doe@gmail.com',\
                     'address':'street 14',\
                     'npa':5678,\
                     'city':'johnland',\
                     'phone':'321/541.43',\
                     'course': 1\
                     }

        self.json_data_participant_put_api_reply = {\
                     'status_api':'success_update',\
                     'status': 'C',\
                     'first_name': 'John',\
                     'last_name': 'Doe',\
                     'birth_date':'2007-07-11',\
                     'gender': 'F',\
                     'email':'john.doe@gmail.com',\
                     'address':'street 14',\
                     'npa':5678,\
                     'city':'johnland',\
                     'phone':'321/541.43',\
                     'course': 1\
                     }

        self.json_data_participant_put_get_verification = {\
                     'id':1,\
                     'status': 'certified',\
                     'first_name': 'John',\
                     'last_name': 'Doe',\
                     'birth_date':'2007-07-11',\
                     'gender': 'F',\
                     'email':'john.doe@gmail.com',\
                     'address':'street 14',\
                     'npa':5678,\
                     'city':'johnland',\
                     'phone':'321/541.43',\
                     'course': 1\
                     }

        self.json_data_participant_put_get_course_verification = {\
                     'id':1,\
                     'status':'open',\
                     'course_type':'samaritains',\
                     'inscription_counter':1,\
                     'max_inscription_counter':12,\
                     'participants':[self.json_data_participant_put_get_verification],\
                     'additional_information':{\
                        'dates':'10-02-2015 10-03-2015',\
                        'location':'Geneva',\
                        'time':'Le cours a lieu de 19h00 a 22h30'}\
                     }

    def date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj


#----------------------------------------------------------


class SamaTestCourse(SamaTestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        super(SamaTestCourse, self).setUp()

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

        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

        request = self.client.put('/api/course/1', self.json_data_course_put, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_put_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_put_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_put_get_verification, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """
        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

        request = self.client.delete('/api/course/1', format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)


#----------------------------------------------------------


class SamaTestParticipant(SamaTestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        super(SamaTestParticipant, self).setUp()

    def test_simple_test(self):
        """
        Simple test
        """
        self.assertEqual(2,2)

    def test_get_empty_db(self):
        """
        Testing GET on an empty database
        """
        request = self.client.get('/api/participant/', {}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

    def test_post_db(self):
        """
        Testing a POST and GET on a database
        """

        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

        request = self.client.post('/api/participant/', self.json_data_participant_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, default=self.date_handler, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_participant_post_api_reply, sort_keys=True))

        request = self.client.get('/api/participant/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_verification, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_course_verification, sort_keys=True))

    def test_put_db(self):
        """
        Testing a POST and GET followed by a PUT and GET on a database
        """

        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

        request = self.client.post('/api/participant/', self.json_data_participant_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, default=self.date_handler, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_participant_post_api_reply, sort_keys=True))

        request = self.client.get('/api/participant/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_verification, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_course_verification, sort_keys=True))

        request = self.client.put('/api/participant/1', self.json_data_participant_put, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.assertEqual(json.dumps(request.data, default=self.date_handler, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant_put_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_participant_put_api_reply, sort_keys=True))

        request = self.client.get('/api/participant/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_put_get_verification, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_put_get_course_verification, sort_keys=True))

    def test_delete_db(self):
        """
        Testing a POST and GET followed by a DELETE and GET on a database
        """

        request = self.client.post('/api/course/', self.json_data_course_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, sort_keys=True), json.dumps(OrderedDict(self.json_data_course_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_course_post_api_reply, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))

        request = self.client.post('/api/participant/', self.json_data_participant_post, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        self.assertEqual(json.dumps(request.data, default=self.date_handler, sort_keys=True), json.dumps(OrderedDict(self.json_data_participant_post_api_reply), sort_keys=True))
        self.assertEqual(json.dumps(json.loads(request.content), sort_keys=True), json.dumps(self.json_data_participant_post_api_reply, sort_keys=True))

        request = self.client.get('/api/participant/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_verification, sort_keys=True))

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_participant_post_get_course_verification, sort_keys=True))

        request = self.client.delete('/api/participant/1', format='json')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        request = self.client.get('/api/participant/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(request.content)), 0)

        request = self.client.get('/api/course/', format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        json_get = ""
        for key in json.loads(request.content):
            json_get = json.dumps(key, sort_keys=True)

        self.assertEqual(json_get, json.dumps(self.json_data_course_post_get_verification, sort_keys=True))
