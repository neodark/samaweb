from rest_framework import serializers
from samacore.models import SamaMember, SamaGroup, CourseType, Date, Course, Participant, Date

class SamaMemberSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaMember data
    """

    class Meta:
        model = SamaMember
        fields = ( 'first_name', 'last_name', 'birth_date', 'sex', 
                   'email', 'address', 'npa', 'city', 'phone', 'id', 'samagroup' )

class SamaGroupSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaGroup data
    """

    thequery = SamaMember.objects.all() 
    samamembers = serializers.PrimaryKeyRelatedField(many=True, queryset=thequery)

    class Meta:
        model = SamaGroup
        fields = ( 'name', 'sama_identifier', 'id', 'samamembers' )

class ParticipantSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaMember data
    """

    class Meta:
        model = Participant
        fields = ( 'first_name', 'last_name', 'birth_date', 'sex',
                   'email', 'address', 'npa', 'city', 'phone',
                   'last_course_date', 'id', 'course' )
 
class DateSerializer( serializers.ModelSerializer ):
   """
   Serializer to parse SamaGroup data
   """

   thequery = Course.objects.all()
   courses = serializers.PrimaryKeyRelatedField(many=True, queryset=thequery)

   class Meta:
       model = Date
       fields = ( 'date', 'end_time', 'id', 'courses' )

class CourseSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaGroup data
    """
    course_dates = DateSerializer(many=True, read_only=True)
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ( 'location', 'inscription_counter', 'max_inscription_counter',
        'status', 'course_type', 'course_dates', 'id', 'participants' )

class CourseTypeSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse CourseType data
    """

    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = CourseType
        fields = ( 'name', 'course_identifier', 'id', 'courses' )

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email',)
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'date_joined',)
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user
