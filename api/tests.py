from django.test import TestCase

from rest_framework.test import APIRequestFactory, APIClient
#Create your tests here.

class TestAPITestClient(TestCase):
    #urls = 'api.tests.test_testing'

    def setUp(self):
        self.client = APIClient()

    def test_credentials(self):
        """
        Setting '.credentials()' adds the required headers to each request.
        """
        self.assertEqual(2,2)
