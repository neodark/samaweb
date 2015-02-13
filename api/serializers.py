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
