from django.db import models
from django_extensions.db.fields import UUIDField

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class SectionManager(models.Manager):

    def create_object(self, section_program={}):

        #Creation of a course
        section             = Section()

        if isinstance(section_program, dict):
            section.section_program = json.dumps(section_program, indent=4)
        else:
            section.section_program = section_program

        ##Adding dates to a course
        #result = course.add_dates(course_dates)
        section.save()

        result = {"success": "all_ok"}

        return (section, result)


class Section(models.Model):

    #_______ Constants _______

    #_______ Fields _______
    section_program         = models.TextField(default='{}', blank=True)

    objects = SectionManager()

    def __str__(self):
        return 'Program:%s'%(self.section_program)

    def save(self, *args, **kwargs):
        super(Section, self).save(*args, **kwargs)


class CourseManager(models.Manager):

    def create_object(self, status, course_type, max_inscription_counter, inscription_counter=0, additional_information={}):

        #Creation of a course
        course              = Course()
        course.status       = self.model.OPEN
        course.course_type  = course_type
        #course.course_dates = course_dates
        course.additional_information = additional_information
        course.inscription_counter = inscription_counter
        course.max_inscription_counter = max_inscription_counter

        if isinstance(additional_information, dict):
            course.additional_information = json.dumps(additional_information, indent=4)
        else:
            course.additional_information = additional_information

        ##Adding dates to a course
        #result = course.add_dates(course_dates)
        course.save()

        result = {"success": "all_ok"}

        return (course, result)

        def open(self):
            return self.filter(status=Course.OPEN)

        def close(self):
            return self.filter(status=Course.CLOSE)


class Course(models.Model):

    #_______ Constants _______

    OPEN = 'O'
    CLOSED = 'C'

    COURSE_STATUS = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    )

    SAUVETEURS = 'A'
    SAMARITAINS = 'B'
    BLSAED = 'D'
    UPE = 'E'

    COURSE_TYPE = (
        (SAUVETEURS, 'Sauveteurs'),
        (SAMARITAINS, 'Samaritains'),
        (BLSAED, 'BLS-AED'),
        (UPE, 'UPE'),
    )

    #_______ Fields _______
    status                  = models.CharField(max_length=1, choices=COURSE_STATUS, default=OPEN)
    course_type             = models.CharField(max_length=1, choices=COURSE_TYPE, default=SAUVETEURS)
    #course_dates            = models.ManyToManyField(DateNew, verbose_name=_("Course Dates"), related_name='coursesnew', blank=True)
    additional_information  = models.TextField(default='{}', blank=True)
    inscription_counter     = models.PositiveIntegerField(_("Inscription Counter"), default=0)
    max_inscription_counter = models.PositiveIntegerField(_("Maximum Inscription Counter"), default=0)

    objects = CourseManager()

    def __str__(self):
        return 'Status:%s - CourseType:%s'%(self.status, self.course_type)

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)

    #def add_dates(course_dates_list):
    #    for course_date in course_dates_list:
    #        self.course_dates.add(course_date)

    #def remove_dates(course_dates_list):
    #    for course_date in course_dates_list:
    #        self.course_dates.remove(course_date)


class ParticipantManager(models.Manager):

    def create_object(self, status, first_name, last_name, birth_date, gender, email, address, npa, city, phone, course):

        #Creation of a course
        participant             = Participant()
        participant.status      = self.model.STUDENT
        participant.first_name  = first_name
        participant.last_name   = last_name
        participant.birth_date  = birth_date
        participant.gender      = gender
        participant.email       = email
        participant.address     = address
        participant.npa         = npa
        participant.city        = city
        participant.phone       = phone
        participant.course      = course

        #result = course.add_dates(course_dates)
        participant.save()

        result = {"success": "all_ok"}

        return (participant, result)

        def male(self):
            return self.filter(gender=Participant.MALE)

        def female(self):
            return self.filter(gender=Participant.FEMALE)


class Participant(models.Model):

    #_______ Constants _______

    STUDENT = 'S'
    UNCOMPLETED = 'U'
    CERTIFIED = 'C'

    PARTICIPANT_STATUS = (
        (STUDENT, 'Student'),
        (UNCOMPLETED, 'Uncompleted'),
        (CERTIFIED, 'Certified'),
    )

    MALE = 'M'
    FEMALE = 'F'

    GENDER_STATUS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    #_______ Fields _______

    status                  = models.CharField(max_length=1, choices=PARTICIPANT_STATUS, default=STUDENT)
    first_name          = models.CharField(_("First Name"), max_length=200)
    last_name           = models.CharField(_("Last Name"), max_length=200)
    birth_date          = models.DateField()
    gender              = models.CharField(max_length=1, choices=GENDER_STATUS, default=MALE)
    email               = models.EmailField(_("Email"))
    address             = models.CharField(_("Address"), max_length=500)
    npa                 = models.IntegerField(_("NPA"), default=0)
    city                = models.CharField(_("City"), max_length=400)
    phone               = models.CharField(_("Phone Number"), max_length=100)
    course              = models.ForeignKey(Course, verbose_name=_("Course Participation"), related_name='participants', blank=True, null=True)
    uuid_field          = UUIDField()

    objects = ParticipantManager()

    def __unicode__(self):
        return '%s %s'%(self.first_name, self.last_name)


    def __str__(self):
        return 'First name:%s - Last Name:%s'%(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(Participant, self).save(*args, **kwargs)
