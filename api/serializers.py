from rest_framework import serializers
from samacore.models import Course
from samacore.models import Participant
from samacore.models import Section
from common.fields import JSONSerializerField

import simplejson as json

class BasicSectionSerializer(serializers.ModelSerializer):
    section_program = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ['id', 'section_program']

    def get_section_program(self, obj):
        return json.loads(obj.section_program)

class CreatedSectionSerializer(BasicSectionSerializer):
    class Meta(BasicSectionSerializer.Meta):
        fields = ['section_program']


class SectionCreationFailedException(Exception):
    pass

class SectionCreationSerializer(serializers.ModelSerializer):
    section_program = JSONSerializerField()

    class Meta:
        model = Section
        fields = ['section_program']

    def create(self, validated_data):
        section = None

        (section, self.details) = self.Meta.model.objects.create_object(**validated_data)
        if section is None:
            raise SectionCreationFailedException()

        return section

    def update(self, instance, validated_data):

        instance.section_program = validated_data.get('section_program', instance.section_program)
        instance.save()

        return instance

    def validate_section_program(self, value):
        return json.dumps(value)


class SectionUpdateSerializer(SectionCreationSerializer):

    class Meta(SectionCreationSerializer.Meta):
        fields = ['section_program']


class BasicParticipantSerializer(serializers.ModelSerializer):
    status  = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name  = serializers.SerializerMethodField()
    birth_date = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    npa = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    #course = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        fields = ['id', 'status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address', 'npa', 'city', 'phone', 'course']

    def get_status(self, obj):
        if obj.status == Participant.STUDENT:
            return 'student'
        elif obj.status == Participant.UNCOMPLETED:
            return 'uncompleted'
        elif obj.status == Participant.CERTIFIED:
            return 'certified'
        else:
            return 'student'

    def get_gender(self, obj):
        if obj.gender == Participant.MALE:
            return 'male'
        elif obj.gender == Participant.FEMALE:
            return 'female'
        else:
            return 'male'

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name

    def get_birth_date(self, obj):
        return obj.birth_date

    def get_gender(self, obj):
        return obj.gender

    def get_email(self, obj):
        return obj.email

    def get_address(self, obj):
        return obj.address

    def get_npa(self, obj):
        return obj.npa

    def get_city(self, obj):
        return obj.city

    def get_phone(self, obj):
        return obj.phone

    def get_course(self, obj):
        return obj.course


class FullParticipantSerializer(BasicParticipantSerializer):
    class Meta(BasicParticipantSerializer.Meta):
        fields = ['id', 'status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address', 'npa', 'city', 'phone', 'course']

class CreatedParticipantSerializer(BasicParticipantSerializer):
    class Meta(BasicParticipantSerializer.Meta):
        fields = ['status', 'course_type', 'additional_information']
        fields = ['status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address', 'npa', 'city', 'phone']


class ParticipantCreationFailedException(Exception):
    pass

class ParticipantCreationSerializer(serializers.ModelSerializer):
    #additional_information = JSONSerializerField()

    class Meta:
        model = Participant
        fields = ['status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address', 'npa', 'city', 'phone', 'course']

    def create(self, validated_data):
        participant = None
        if not validated_data.has_key('status'):
            raise serializers.ValidationError('Participant status not specified')
        if not validated_data.has_key('first_name'):
            raise serializers.ValidationError('Participant first_name not specified')
        if not validated_data.has_key('last_name'):
            raise serializers.ValidationError('Participant last_name not specified')
        if not validated_data.has_key('birth_date'):
            raise serializers.ValidationError('Participant birth_date not specified')
        if not validated_data.has_key('gender'):
            raise serializers.ValidationError('Participant gender not specified')
        if not validated_data.has_key('email'):
            raise serializers.ValidationError('Participant email not specified')
        if not validated_data.has_key('address'):
            raise serializers.ValidationError('Participant address not specified')
        if not validated_data.has_key('npa'):
            raise serializers.ValidationError('Participant npa not specified')
        if not validated_data.has_key('city'):
            raise serializers.ValidationError('Participant city not specified')
        if not validated_data.has_key('phone'):
            raise serializers.ValidationError('Participant phone not specified')
        if not validated_data.has_key('course'):
            raise serializers.ValidationError('Participant course not specified')

        (participant, self.details) = self.Meta.model.objects.create_object(**validated_data)
        if participant is None:
            raise ParticipantCreationFailedException()

        return participant

    def update(self, instance, validated_data):

        instance.status = validated_data.get('status', instance.status)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.npa = validated_data.get('npa', instance.npa)
        instance.city = validated_data.get('city', instance.city)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.course = validated_data.get('course', instance.course)
        instance.save()

        return instance

    def validate_status(self, value):
        return value

    def validate_first_name(self, value):
        return value

    def validate_last_name(self, value):
        return value

    def validate_birth_date(self, value):
        return value

    def validate_gender(self, value):
        return value

    def validate_email(self, value):
        return value

    def validate_npa(self, value):
        return value

    def validate_city(self, value):
        return value

    def validate_phone(self, value):
        return value

    def validate_course(self, value):
        return value


class ParticipantUpdateSerializer(ParticipantCreationSerializer):

    class Meta(ParticipantCreationSerializer.Meta):
        fields = ['status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address', 'npa', 'city', 'phone', 'course']


class BasicCourseSerializer(serializers.ModelSerializer):
    status  = serializers.SerializerMethodField()
    course_type = serializers.SerializerMethodField()
    #course_dates = serializers.SerializerMethodField()
    additional_information = serializers.SerializerMethodField()
    inscription_counter = serializers.SerializerMethodField()
    max_inscription_counter = serializers.SerializerMethodField()
    participants = BasicParticipantSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'status', 'course_type', 'additional_information', 'inscription_counter', 'max_inscription_counter', 'participants']

    def get_status(self, obj):
        if obj.status == Course.OPEN:
            return 'open'
        elif obj.status == Course.CLOSED:
            return 'closed'
        else:
            return 'open'

    def get_course_type(self, obj):
        if obj.course_type == Course.SAUVETEURS:
            return 'sauveteurs'
        elif obj.course_type == Course.SAMARITAINS:
            return 'samaritains'
        elif obj.course_type == Course.BLSAED:
            return 'bls-aed'
        elif obj.course_type == Course.UPE:
            return 'upe'
        else:
            return 'sauveteurs'

    #def get_course_dates(self, obj):
    #    return map(lambda x: x, obj.course_dates.iterator())

    def get_additional_information(self, obj):
        return json.loads(obj.additional_information)

    def get_inscription_counter(self, obj):
        return obj.inscription_counter

    def get_max_inscription_counter(self, obj):
        return obj.max_inscription_counter

class FullCourseSerializer(BasicCourseSerializer):
    class Meta(BasicCourseSerializer.Meta):
        fields = ['id', 'status', 'course_type', 'additional_information', 'inscription_counter', 'max_inscription_counter']

class CreatedCourseSerializer(BasicCourseSerializer):
    class Meta(BasicCourseSerializer.Meta):
        fields = ['status', 'course_type', 'additional_information']


class CourseCreationFailedException(Exception):
    pass

class CourseCreationSerializer(serializers.ModelSerializer):
    additional_information = JSONSerializerField()
    #course_dates = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Course
        fields = ['status', 'course_type', 'inscription_counter', 'max_inscription_counter', 'additional_information']

    def create(self, validated_data):
        course = None
        if not validated_data.has_key('course_type'):
            raise serializers.ValidationError('Course type not specified')

        (course, self.details) = self.Meta.model.objects.create_object(**validated_data)
        if course is None:
            raise CourseCreationFailedException()

        return course

    def update(self, instance, validated_data):

        instance.status = validated_data.get('status', instance.status)
        instance.course_type = validated_data.get('course_type', instance.course_type)
        instance.inscription_counter = validated_data.get('inscription_counter', instance.inscription_counter)
        instance.max_inscription_counter = validated_data.get('max_inscription_counter', instance.max_inscription_counter)
        instance.additional_information = validated_data.get('additional_information', instance.additional_information)
        instance.save()

        if validated_data.has_key('status'):
            if len(self.data["participants"]) > 0:
                for participant_id in self.data["participants"]:
                    participant = Participant.objects.get(id=participant_id)
                    if instance.status == Course.CLOSED:
                        participant.status = Participant.CERTIFIED
                    else:
                        participant.status = Participant.STUDENT
                    participant.save()

        return instance


    def validate_status(self, value):
        return value

    def validate_course_type(self, value):
        return value

    def validate_inscription_counter(self, value):
        return value

    def validate_max_inscription_counter(self, value):
        return value

    def validate_additional_information(self, value):
        return json.dumps(value)

    #def validate_course_dates(self, value):
    #    return value

    #def to_representation(self, obj):
    #    serializer = CreatedCourseSerializer(obj, context=self.context)
    #    return serializer.data


class CourseUpdateSerializer(CourseCreationSerializer):

    class Meta(CourseCreationSerializer.Meta):
        fields = ['status', 'course_type', 'inscription_counter', 'max_inscription_counter', 'additional_information', 'participants']

    #def to_representation(self, obj):
    #    serializer = CourseUpdateSerializer(obj)
    #    return serializer.data

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
