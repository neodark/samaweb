from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from api.serializers import UserSerializer

from samacore.models import Course
from api.serializers import BasicCourseSerializer, CourseCreationSerializer, CourseUpdateSerializer

from api.serializers import CourseCreationFailedException

from samacore.models import Participant
from api.serializers import BasicParticipantSerializer, ParticipantCreationSerializer, ParticipantUpdateSerializer

from api.serializers import ParticipantCreationFailedException

from rest_framework.views import APIView

#For UserView and AuthView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import IsStaffOrTargetUser

from . import authentication, serializers

import simplejson as json
# Create your views here.

# Class based views

class CourseCreationNewView(ListCreateAPIView):
    """
    List/Create APIView
    """
    model = Course
    serializer_class = BasicCourseSerializer
    writing_serializer_class =  CourseCreationSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            self.serializer_class = self.writing_serializer_class

        return super(CourseCreationNewView, self).get_serializer(*args, **kwargs)

    def list(self, request):
        queryset = Course.objects.all()

        #self.request.QUERY_PARAMS.has_key('coursetype')
        coursetype = self.request.QUERY_PARAMS.get('coursetype', None)

        #Filter course by course type if requested
        if coursetype is not None:
            for key, value in Course.COURSE_TYPE:
                if value == coursetype:
                    queryset = queryset.filter(course_type=key)
                    break

        #sorting queryset course by date
        idx_course = 0
        course_to_sort = []
        course_idx = {}
        for item in queryset:
            additional_information = json.loads(item.additional_information)
            if additional_information.has_key('dates'):
                dates = additional_information['dates']
                if len(dates.split(' ')) > 1:
                    course_list=[]
                    for date in dates.split(' '):
                        course_list.append(date)
                    sorted_course_list = sorted(course_list, key=lambda d: map(int, reversed(d.split('-'))))
                    course_to_sort.append(sorted_course_list[0])
                    course_idx[sorted_course_list[0]] = idx_course
                else:
                    course_to_sort.append(dates)
                    course_idx[dates] = idx_course
                idx_course +=1

        sorted_course_list = sorted(course_to_sort, key=lambda d: map(int, reversed(d.split('-'))))
        tempqueryset = []
        for course in sorted_course_list:
            tempqueryset.append(queryset[course_idx[course]])
        queryset = tempqueryset

        serializer = BasicCourseSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        if request.data["course_type"] is not None:
            for key, value in Course.COURSE_TYPE:
                if value == request.data["course_type"]:
                    request.data["course_type"] = key
                    break

        serializer = self.get_serializer(data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            course = serializer.save()
        except CourseCreationFailedException:
            pass

        details = serializer.details

        if details['success']:
            result = {
                'coursename' : 'ok',
                'course' : course.status
            }
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return BadRequestResponse()

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    model = Course
    serializer_class = BasicCourseSerializer
    writing_serializer_class = CourseUpdateSerializer

    def get_queryset(self, object_id):
        #queryset = Course.objects.all()
        queryset = Course.objects.get(id=object_id)
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            self.serializer_class = self.writing_serializer_class

        return super(CourseDetailView, self).get_serializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.kwargs.has_key('pk'):
            course = self.get_queryset(self.kwargs.get('pk'))
            serializer = self.serializer_class(course, context={'request': request})
            data = serializer.data

            return Response(data)

    def delete(self, request, *args, **kwargs):
        if self.kwargs.has_key('pk'):
            course = self.get_queryset(self.kwargs.get('pk'))
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # Process the query string
        if request.GET.has_key('fields'):
            fields_to_return = request.GET['fields'].split(',')
        else:
            # Available fields (not returned by default):
            #    - html_description
            fields_to_return = []

        if self.kwargs.has_key('pk'):
            course = self.get_queryset(self.kwargs.get('pk'))

            serializer = self.writing_serializer_class(course, data=request.data, partial=True)
            if not(serializer.is_valid()):
                return BadRequestResponse(serializer.errors)

            db_object = serializer.save()
            #details = serializer.details

            result = {
                'update': 'updated'
            }

            response = Response(result, status=status.HTTP_200_OK)
            #response['Location'] = result['url']
            return response

class ParticipantCreationView(ListCreateAPIView):
    """
    List/Create APIView
    """
    model = Participant
    serializer_class = BasicParticipantSerializer
    writing_serializer_class =  ParticipantCreationSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            self.serializer_class = self.writing_serializer_class

        return super(ParticipantCreationView, self).get_serializer(*args, **kwargs)

    def list(self, request):
        queryset = Participant.objects.all()
        serializer = BasicParticipantSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            participant = serializer.save()

            course = Course.objects.get(id=participant.course.id)
            course.inscription_counter = course.participants.count()
            course.save()
        except ParticipantCreationFailedException:
            pass

        details = serializer.details

        if details['success']:
            result = {
                'coursename' : 'ok',
                'course' : participant.status
            }
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return BadRequestResponse()

class ParticipantDetailView(RetrieveUpdateDestroyAPIView):
    model = Participant
    serializer_class = BasicParticipantSerializer
    writing_serializer_class = ParticipantUpdateSerializer

    def get_queryset(self, object_id):
        queryset = Participant.objects.get(id=object_id)
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            self.serializer_class = self.writing_serializer_class

        return super(ParticipantDetailView, self).get_serializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.kwargs.has_key('pk'):
            participant = self.get_queryset(self.kwargs.get('pk'))
            serializer = self.serializer_class(participant, context={'request': request})
            data = serializer.data

            return Response(data)

    def delete(self, request, *args, **kwargs):
        if self.kwargs.has_key('pk'):
            participant = self.get_queryset(self.kwargs.get('pk'))

            course = Course.objects.get(id=participant.course.id)

            participant.delete()

            course.inscription_counter = course.participants.count()
            course.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # Process the query string
        if request.GET.has_key('fields'):
            fields_to_return = request.GET['fields'].split(',')
        else:
            # Available fields (not returned by default):
            #    - html_description
            fields_to_return = []

        if self.kwargs.has_key('pk'):
            participant = self.get_queryset(self.kwargs.get('pk'))

            serializer = self.writing_serializer_class(participant, data=request.data, partial=True)
            if not(serializer.is_valid()):
                return BadRequestResponse(serializer.errors)

            db_object = serializer.save()
            #details = serializer.details

            result = {
                'update': 'updated'
            }

            response = Response(result, status=status.HTTP_200_OK)
            #response['Location'] = result['url']
            return response


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


class AuthView(APIView):
    authentication_classes = (authentication.QuietBasicAuthentication,)
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        #Decode in base 64 and retrieve username and password
        import base64
        username = base64.standard_b64decode(request.data["username"])
        password = base64.standard_b64decode(request.data["password"])
        user = authenticate(username=username, password=password)
        login(request, user)
        return Response(serializers.UserSerializer(user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()
