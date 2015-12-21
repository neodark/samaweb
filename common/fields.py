from rest_framework import serializers

import simplejson
import six


class StringListField(serializers.ListField):
    child = serializers.CharField()


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            return simplejson.loads(data)
        return data

    def to_representation(self, value):
        return value
