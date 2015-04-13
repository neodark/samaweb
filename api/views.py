from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from samacore.models import SamaMember, SamaGroup, Participant, Date, Course, CourseType
from api.serializers import SamaMemberSerializer, SamaGroupSerializer, ParticipantSerializer, DateSerializer, CourseSerializer, CourseTypeSerializer

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
