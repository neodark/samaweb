from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from api.serializers import UserSerializer

from samacore.models import Section
from api.serializers import BasicSectionSerializer, SectionCreationSerializer, SectionUpdateSerializer

from api.serializers import SectionCreationFailedException


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
from rest_framework import permissions
from rest_framework.permissions import AllowAny

from .permissions import IsStaffOrTargetUser

from . import authentication, serializers

import simplejson as json

from common.responses import BadRequestResponse, ForbiddenResponse

#For email confirmation
#from common.models import EmailMultiRelated
from django.core.mail import EmailMessage
from django.conf import settings
from django.conf.urls.static import static


# Create your views here.

# Class based views

class SectionCreationNewView(ListCreateAPIView):
    """
    List/Create APIView
    """
    model = Section
    serializer_class = BasicSectionSerializer
    writing_serializer_class =  SectionCreationSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            self.serializer_class = self.writing_serializer_class

        return super(SectionCreationNewView, self).get_serializer(*args, **kwargs)

    def list(self, request):
        queryset = Section.objects.all()

        serializer = BasicSectionSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):

        serializer = self.get_serializer(data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            section = serializer.save()
        except SectionCreationFailedException:
            pass

        details = serializer.details

        if details['success']:
            result = {
                'status_api' : 'success_creation',
                'section_program' : section.section_program,
            }
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return BadRequestResponse()

class SectionDetailView(RetrieveUpdateDestroyAPIView):
    model = Section
    serializer_class = BasicSectionSerializer
    writing_serializer_class = SectionUpdateSerializer

    def get_queryset(self, object_id):
        #queryset = Section.objects.all()
        queryset = Section.objects.get(id=object_id)
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            self.serializer_class = self.writing_serializer_class

        return super(SectionDetailView, self).get_serializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            section = self.get_queryset(self.kwargs.get('pk'))
            serializer = self.serializer_class(section, context={'request': request})
            data = serializer.data

            return Response(data)

    def delete(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            section = self.get_queryset(self.kwargs.get('pk'))
            section.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # Process the query string
        if 'fields' in request.GET:
            fields_to_return = request.GET['fields'].split(',')
        else:
            # Available fields (not returned by default):
            #    - html_description
            fields_to_return = []

        if 'pk' in self.kwargs:
            section = self.get_queryset(self.kwargs.get('pk'))

            serializer = self.writing_serializer_class(section, data=request.data, partial=True)
            if not(serializer.is_valid()):
                return BadRequestResponse(serializer.errors)

            db_object = serializer.save()
            #details = serializer.details

            result = {
                'status_api' : 'success_update',
                'section_program' : section.section_program,
            }

            response = Response(result, status=status.HTTP_200_OK)
            #response['Location'] = result['url']
            return response


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

        #self.request.query_params.has_key('coursetype')
        coursetype = self.request.query_params.get('coursetype', None)
        coursestatus = self.request.query_params.get('coursestatus', None)

        #Filter course by course type if requested
        if coursetype is not None:
            for key, value in Course.COURSE_TYPE:
                if value == coursetype:
                    queryset = queryset.filter(course_type=key)
                    break

        #Filter course by course status if requested
        if coursestatus is not None:
            for key, value in Course.COURSE_STATUS:
                if value == coursestatus:
                    queryset = queryset.filter(status=key)
                    break

        #sorting queryset course by date
        idx_course = 0
        course_to_sort = []
        course_idx = {}
        for item in queryset:
            additional_information = json.loads(item.additional_information)
            if 'dates' in additional_information:
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

        if len(course_to_sort) > 0:
            sorted_course_list = sorted(course_to_sort, key=lambda d: map(int, reversed(d.split('-'))))
        else:
            sorted_course_list = []

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
                'status_api' : 'success_creation',
                'status' : course.status,
                'course_type' : course.course_type,
                'max_inscription_counter' : course.max_inscription_counter,
                'additional_information' : course.additional_information,
                'course_price' : course.course_price,
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
        if 'pk' in self.kwargs:
            course = self.get_queryset(self.kwargs.get('pk'))
            serializer = self.serializer_class(course, context={'request': request})
            data = serializer.data

            return Response(data)

    def delete(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            course = self.get_queryset(self.kwargs.get('pk'))
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # Process the query string
        if 'fields' in request.GET:
            fields_to_return = request.GET['fields'].split(',')
        else:
            # Available fields (not returned by default):
            #    - html_description
            fields_to_return = []

        if request.data["course_type"] is not None:
            for key, value in Course.COURSE_TYPE:
                if value == request.data["course_type"]:
                    request.data["course_type"] = key
                    break

        if 'pk' in self.kwargs:
            course = self.get_queryset(self.kwargs.get('pk'))

            serializer = self.writing_serializer_class(course, data=request.data, partial=True)
            if not(serializer.is_valid()):
                return BadRequestResponse(serializer.errors)

            db_object = serializer.save()
            #details = serializer.details

            result = {
                'status_api' : 'success_update',
                'status' : course.status,
                'course_type' : course.course_type,
                'max_inscription_counter' : course.max_inscription_counter,
                'additional_information' : course.additional_information,
                'course_price' : course.course_price,
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

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]

        self.permission_classes = permission_classes

        return super(ParticipantCreationView, self).get_permissions()

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

        f = open(settings.STATICFILES_DIRS[0] + '/data/email_message.txt', 'r')
        data_email=f.readlines()
        f.close()

        logo = open(settings.STATICFILES_DIRS[0] + '/data/logo_martigny_small.png', 'r')
        logo_data = logo.read()

        logo_data_base_64 = logo_data.encode("base64")
        logo.close()

        additional_information = json.loads(course.additional_information)

        mydict = {}

        mydict["__TAG_LOGO__"] = '<div><img src="data:image/png;base64,' + logo_data_base_64 + '">'

        first_name = participant.first_name
        last_name = participant.last_name
        first_name_decoded = first_name.encode('utf-8')
        last_name_decoded = last_name.encode('utf-8')

        if participant.gender == 'F':
            mydict["__TAG_PERSON__"] = "Mme. " + first_name_decoded + " " + last_name_decoded
        else:
            mydict["__TAG_PERSON__"] = "M. " + first_name_decoded + " " + last_name_decoded

        for key, value in Course.COURSE_TYPE:
            if key == course.course_type:
                mydict["__TAG_COURSE_TYPE__"] = "%s"%value
                break

        mydict["__TAG_COURSE_PRICE__"] = "%s"%course.course_price

        mydict["__TAG_COURSE_DATES__"] = "%s"%additional_information["dates"].encode('utf-8')
        mydict["__TAG_COURSE_TIME__"] = "%s"%additional_information["time"].encode('utf-8')
        mydict["__TAG_COURSE_LOCATION__"] = "%s"%additional_information["location"].encode('utf-8')
        tags = ["__TAG_LOGO__", "__TAG_PERSON__", "__TAG_COURSE_TYPE__", "__TAG_COURSE_PRICE__", "__TAG_COURSE_DATES__",
                "__TAG_COURSE_TIME__", "__TAG_COURSE_LOCATION__"]

        final_text = ""
        final_list = []
        for text in data_email:
            text_decoded = text.decode('utf-8').encode('utf-8')
            if any(s in text_decoded for s in tags):
                for tag in tags:
                    if tag in text_decoded:
                        replaced_text = text_decoded.replace(tag, mydict[tag])
                        replaced_text_decoded = text_decoded.replace(tag, mydict[tag]).decode('utf-8').encode('utf-8')
                        final_list.append(replaced_text_decoded)
            else:
                final_list.append(text_decoded)

        for item_email in final_list:
            final_text += item_email

        msg = EmailMessage("Confirmation inscription au cours", final_text, to=[participant.email])
        msg.content_subtype = 'html'
        try:
            msg.send()
        except:
            pass

        if details['success']:
            result = {
                'status_api' : 'success_creation',
                'status' : participant.status,
                'first_name' : participant.first_name,
                'last_name' : participant.last_name,
                'birth_date' : participant.birth_date,
                'gender' : participant.gender,
                'email' : participant.email,
                'address' : participant.address,
                'npa' : participant.npa,
                'city' : participant.city,
                'phone' : participant.phone,
                'course' : participant.course.id,
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
        if 'pk' in self.kwargs:
            participant = self.get_queryset(self.kwargs.get('pk'))
            serializer = self.serializer_class(participant, context={'request': request})
            data = serializer.data

            return Response(data)

    def delete(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            participant = self.get_queryset(self.kwargs.get('pk'))

            course = Course.objects.get(id=participant.course.id)

            participant.delete()

            course.inscription_counter = course.participants.count()
            course.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        # Process the query string
        if 'fields' in request.GET:
            fields_to_return = request.GET['fields'].split(',')
        else:
            # Available fields (not returned by default):
            #    - html_description
            fields_to_return = []

        if 'pk' in self.kwargs:
            participant = self.get_queryset(self.kwargs.get('pk'))

            serializer = self.writing_serializer_class(participant, data=request.data, partial=True)
            if not(serializer.is_valid()):
                return BadRequestResponse(serializer.errors)

            db_object = serializer.save()
            #details = serializer.details

            result = {
                'status_api' : 'success_update',
                'status' : participant.status,
                'first_name' : participant.first_name,
                'last_name' : participant.last_name,
                'birth_date' : participant.birth_date,
                'gender' : participant.gender,
                'email' : participant.email,
                'address' : participant.address,
                'npa' : participant.npa,
                'city' : participant.city,
                'phone' : participant.phone,
                'course' : participant.course.id,
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
        #Check if user has been successfully authenticated
        if user != None:
            login(request, user)
        return Response(serializers.UserSerializer(user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()
