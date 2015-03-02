from rest_framework import serializers
from samacore.models import SamaMember, SamaGroup, CourseType, Course, Participant, Date

class SamaMemberSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse SamaMember data
	"""

	class Meta:
		model = SamaMember
		fields = ( 'first_name', 'last_name', 'birth_date', 'sex', 
                   'email', 'address', 'npa', 'city', 'phone', 'id' )

class SamaGroupSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse SamaGroup data
	"""

	class Meta:
		model = SamaGroup
		fields = ( 'name', 'type', 'samamember', 'id' )
        extra_kwargs = {
            'samamember': {'required':False}
        }

class CourseTypeSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse CourseType data
	"""

	class Meta:
		model = CourseType
		fields = ( 'name', 'type', 'id' )
