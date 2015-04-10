from rest_framework import serializers
from samacore.models import SamaMember, SamaGroup, CourseType, Course, Participant, Date

class SamaMemberSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaMember data
    """
    #samagroups = SamaGroupSerializer(many=True, required=False)

    class Meta:
        model = SamaMember
        fields = ( 'first_name', 'last_name', 'birth_date', 'sex', 
                   'email', 'address', 'npa', 'city', 'phone', 'id', 'samagroup' )
                   #'email', 'address', 'npa', 'city', 'phone', 'id', 'samagroups' )

    #def create(self, validated_data):
    #    #samagroups_data = validated_data.pop('samagroups')
    #    samamember = SamaMember.objects.create(**validated_data)
    #    #samagroup = SamaGroup.objects.create(samamember=samamember, **samagroups_data)
    #    for sam in samamember:
    #        d=dict(sam)
    #        SamaGroup.objects.create(group=group, sam=d['person'])
    #        return group
    #    #for sam in samagroups_data:
    #    #    d=dict(sam)
    #    #    SamaGroup.objects.create(group=group, sam=d['person'])
    #    #    return group

    #	return samamember
    #def create(self, validated_data):
    #	#samagroups_data = validated_data.pop('samagroups')
    #	samamember = SamaMember.objects.create(**validated_data)
    #	#samagroup = SamaGroup.objects.create(samamember=samamember, **samagroups_data)
    #	for sam in samamember:
    #	    d=dict(sam)
    #	    SamaGroup.objects.create(group=group, sam=d['person'])
    #	    return group
    #	#for sam in samagroups_data:
    #	#    d=dict(sam)
    #	#    SamaGroup.objects.create(group=group, sam=d['person'])
    #	#    return group

    #	return samamember

class SamaGroupSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaGroup data
    """
    #samamember_name = serializers.RelatedField(source='samamember')
    #samamembers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #samamembers = SamaMemberSerializer(
    #        source = 'get_samamembers',
    #        #read_only=True
    #)
    thequery = SamaGroup.get_samamembers 
    thequery = SamaMember.objects.all() 


    #samamembers = serializers.PrimaryKeyRelatedField(many=True, queryset=SamaMember.objects.all(), read_only=True)
    samamembers = serializers.PrimaryKeyRelatedField(many=True, queryset=thequery)
    #samamembers = serializers.ManytoManyField(many=True, queryset=thequery)
    #print samamembers

    class Meta:
        model = SamaGroup
        #fields = ( 'name', 'type', 'samamember_name', 'id' )
        #fields = ( 'name', 'type', 'samamember', 'id' )
        #fields = ( 'name', 'sama_identifier', 'id', 'samamembers' )
        fields = ( 'name', 'sama_identifier', 'id', 'samamembers' )
        #fields = ( 'name', 'sama_identifier', 'id', 'samagroup' )
        #extra_kwargs = {
        #    'samamember': {'required':False}
        #}

class ParticipantSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaMember data
    """
    #samagroups = SamaGroupSerializer(many=True, required=False)

    class Meta:
        model = Participant
        fields = ( 'first_name', 'last_name', 'birth_date', 'sex', 
                   'email', 'address', 'npa', 'city', 'phone', 'id', 'course' )
 
class CourseSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse SamaGroup data
    """
    #samamember_name = serializers.RelatedField(source='samamember')
    #samamembers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #samamembers = SamaMemberSerializer(
    #        source = 'get_samamembers',
    #        #read_only=True
    #)
    thequery = Participant.objects.all() 


    #samamembers = serializers.PrimaryKeyRelatedField(many=True, queryset=SamaMember.objects.all(), read_only=True)
    participants = serializers.PrimaryKeyRelatedField(many=True, queryset=thequery)
    #samamembers = serializers.ManytoManyField(many=True, queryset=thequery)
    #print samamembers

    class Meta:
        model = Course
        #fields = ( 'name', 'type', 'samamember_name', 'id' )
        #fields = ( 'name', 'type', 'samamember', 'id' )
        #fields = ( 'name', 'sama_identifier', 'id', 'samamembers' )
        fields = ( 'location', 'inscription_counter', 'max_inscription_counter',
        'status', 'course_type', 'id', 'participants' )
        #fields = ( 'name', 'sama_identifier', 'id', 'samagroup' )
        #extra_kwargs = {
        #    'samamember': {'required':False}
        #}

class CourseTypeSerializer( serializers.ModelSerializer ):
    """
    Serializer to parse CourseType data
    """

    thequery = Course.objects.all() 

    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=thequery)

    class Meta:
        model = CourseType
        fields = ( 'name', 'course_identifier', 'id', 'courses' )
