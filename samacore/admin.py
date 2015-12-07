from django.contrib import admin

from samacore.models import CourseNewVersion
from samacore.models import ParticipantNew

# Register your models here.

class CourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'status', 'course_type', 'inscription_counter', 'max_inscription_counter', 'additional_information')

admin.site.register(CourseNewVersion, CourseAdmin)

class ParticipantAdmin(admin.ModelAdmin):

    list_display = ('id', 'status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address',
                    'npa', 'city', 'phone', 'course', 'uuid_field')

admin.site.register(ParticipantNew, ParticipantAdmin)
