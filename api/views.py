from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from samacore.models import SamaMember, CourseType
from api.serializers import SamaMemberSerializer, CourseTypeSerializer

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
