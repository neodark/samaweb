from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from samacore.models import SamaMember, SamaGroup, Participant, Date, Course, CourseType

from api.serializers import SamaMemberSerializer, SamaGroupSerializer, ParticipantSerializer, DateSerializer, CourseSerializer, CourseTypeSerializer, UserSerializer

from samacore.models import CourseNewVersion
from api.serializers import BasicCourseSerializer, CourseNewVersionCreationSerializer, CourseUpdateSerializer

from api.serializers import CourseCreationFailedException

from samacore.models import ParticipantNew
from api.serializers import BasicParticipantSerializer, ParticipantCreationSerializer, ParticipantUpdateSerializer

from api.serializers import ParticipantCreationFailedException

from rest_framework.views import APIView

#For UserView and AuthView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import IsStaffOrTargetUser

from . import authentication, serializers  # see previous post[1] for user serializer.

# Create your views here.

# Class based views

class SamaMemberMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = SamaMember.objects.all()
    serializer_class = SamaMemberSerializer

class SamaMemberList(SamaMemberMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """
    pass

class SamaMemberDetail(SamaMemberMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class ParticipantMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantList(ParticipantMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """
    pass

class ParticipantDetail(ParticipantMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class DateMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Date.objects.all()
    serializer_class = DateSerializer

class DateList(DateMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """
    pass

class DateDetail(DateMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class CourseMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseList(CourseMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """

    def get_queryset(self):
        queryset = Course.objects.all()
        coursetype = self.request.QUERY_PARAMS.get('coursetype', None)
        if coursetype is not None:
            queryset = queryset.filter(course_type__name=coursetype)
        return queryset

    pass

class CourseDetail(CourseMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class CourseTypeMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer

class CourseTypeList(CourseTypeMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """
    pass

class CourseTypeDetail(CourseTypeMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class SamaGroupMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = SamaGroup.objects.all()
    serializer_class = SamaGroupSerializer

class SamaGroupList(SamaGroupMixin, ListCreateAPIView):
    """
    Return a list of all the SamaMembers, or
    create new ones
    """
    pass

class SamaGroupDetail(SamaGroupMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific SamaMember, update it, or delete it.
    """
    pass

class CourseCreationNewView(ListCreateAPIView):
    """
    List/Create APIView
    """
    model = CourseNewVersion
    serializer_class = BasicCourseSerializer
    writing_serializer_class =  CourseNewVersionCreationSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            self.serializer_class = self.writing_serializer_class

        return super(CourseCreationNewView, self).get_serializer(*args, **kwargs)

    def list(self, request):
        queryset = CourseNewVersion.objects.all()

        #self.request.QUERY_PARAMS.has_key('coursetype')
        coursetype = self.request.QUERY_PARAMS.get('coursetype', None)

        #Filter course by course type if requested
        if coursetype is not None:
            for key, value in CourseNewVersion.COURSE_TYPE:
                if value == coursetype:
                    queryset = queryset.filter(course_type=key)
                    break

        serializer = BasicCourseSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
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
    model = CourseNewVersion
    serializer_class = BasicCourseSerializer
    writing_serializer_class = CourseUpdateSerializer

    def get_queryset(self, object_id):
        #queryset = CourseNewVersion.objects.all()
        queryset = CourseNewVersion.objects.get(id=object_id)
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

class ParticipantNewCreationView(ListCreateAPIView):
    """
    List/Create APIView
    """
    model = ParticipantNew
    serializer_class = BasicParticipantSerializer
    writing_serializer_class =  ParticipantCreationSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            self.serializer_class = self.writing_serializer_class

        return super(ParticipantNewCreationView, self).get_serializer(*args, **kwargs)

    def list(self, request):
        queryset = ParticipantNew.objects.all()
        serializer = BasicParticipantSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            participant = serializer.save()
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
    model = ParticipantNew
    serializer_class = BasicParticipantSerializer
    writing_serializer_class = ParticipantUpdateSerializer

    def get_queryset(self, object_id):
        queryset = ParticipantNew.objects.get(id=object_id)
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
            participant.delete()
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
