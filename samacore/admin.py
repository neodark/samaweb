from django.contrib import admin

from samacore.models import Course
from samacore.models import Participant

# Register your models here.

class CourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'status', 'course_type', 'inscription_counter', 'max_inscription_counter', 'additional_information', 'course_price')

admin.site.register(Course, CourseAdmin)

class ParticipantAdmin(admin.ModelAdmin):

    list_display = ('id', 'status', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'address',
                    'npa', 'city', 'phone', 'course', 'uuid_field')

admin.site.register(Participant, ParticipantAdmin)
