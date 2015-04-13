from django.db import models
from django_extensions.db.fields import UUIDField

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class SamaGroup(models.Model):
    name                = models.CharField(_("Sama Group Name"), max_length=120)
    sama_identifier     = models.PositiveIntegerField(_("Sama Type Identifier"), default=0)
    def __unicode__(self):
        return '%s'%(self.name)

    def get_samamembers(self):
        samamembers = SamaMember.objects.all()
        return samamembers

class SamaMember(models.Model):
    first_name          = models.CharField(_("First Name"), max_length=70)
    last_name           = models.CharField(_("Last Name"), max_length=70)
    birth_date          = models.DateField()
    sex                 = models.PositiveIntegerField(_("Sex"), default=0)
    email               = models.EmailField(_("Email"))
    address             = models.CharField(_("Address"), max_length=120)
    npa                 = models.PositiveIntegerField(_("NPA"), default=0)
    city                = models.CharField(_("City"), max_length=50)
    phone               = models.CharField(_("Phone Number"), max_length=30)
    samagroup           = models.ManyToManyField(SamaGroup, verbose_name=_("Sama Member Group"), related_name='samamembers', blank=True, null=True)
    def __unicode__(self):
        return '%s %s'%(self.first_name, self.last_name)

class CourseType(models.Model):
    name                = models.CharField(_("Course Type Name"), max_length=120)
    course_identifier   = models.PositiveIntegerField(_("Course Type Identifier"), default=0)
    def __str__(self):
        return '%s'%(self.name)

class Date(models.Model):
    date                = models.DateTimeField()
    def __str__(self):
        return '%s'%(self.date)

class Course(models.Model):
    course_dates    = models.ManyToManyField(Date, verbose_name=_("Course Dates"), related_name='courses', blank=True, null=True)
    location            = models.CharField(_("Course Location"), max_length=300)
    inscription_counter     = models.PositiveIntegerField(_("Inscription Counter"), default=0)
    max_inscription_counter = models.PositiveIntegerField(_("Maximum Inscription Counter"), default=0)
    status              = models.BooleanField(_("Course Status"), default=True)
    course_type         = models.ForeignKey(CourseType, verbose_name=_("Type of Course"), related_name='courses', blank=True, null=True)
    def __str__(self):
        return 'Location:%s - CourseType:%s'%(self.location, self.course_type)

class Participant(models.Model):
    first_name          = models.CharField(_("First Name"), max_length=70)
    last_name           = models.CharField(_("Last Name"), max_length=70)
    birth_date          = models.DateField()
    sex                 = models.IntegerField(_("Sex"), default=0)
    email               = models.EmailField(_("Email"))
    address             = models.CharField(_("Address"), max_length=120)
    npa                 = models.IntegerField(_("NPA"), default=0)
    city                = models.CharField(_("City"), max_length=50)
    phone               = models.CharField(_("Phone Number"), max_length=30)
    course              = models.ForeignKey(Course, verbose_name=_("Course Participation"), related_name='participants', blank=True, null=True)
    last_course_date    = models.DateField()
    uuid_field          = UUIDField()
    def __unicode__(self):
        return '%s %s'%(self.first_name, self.last_name)
