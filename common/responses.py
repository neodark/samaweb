from rest_framework.response import Response
from rest_framework import status

class BadRequestResponse(Response):
    def __init__(self, data):
        super(BadRequestResponse, self).__init__(data, status=status.HTTP_400_BAD_REQUEST)

class ForbiddenResponse(Response):
    def __init__(self, data=''):
        super(ForbiddenResponse, self).__init__(data, status=status.HTTP_403_FORBIDDEN)
