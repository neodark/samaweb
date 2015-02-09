from django.db import models
from django_extensions.db.fields import UUIDField

# Create your models here.

class SamaMember(models.Model):
    first_name      = models.CharField(max_length=70)
    last_name       = models.CharField(max_length=70)
    birth_date      = models.DateField()
    sex             = models.IntegerField()
    email           = models.EmailField()
    address         = models.CharField(max_length=120)
    npa             = models.IntegerField()
    city            = models.CharField(max_length=50)
    phone           = models.CharField(max_length=30)
    headshot        = models.ImageField(upload_to='/tmp')
    def __unicode__(self):
        return '%s %s'%(self.first_name, self.last_name)

class SamaGroup(models.Model):
    name            = models.CharField(max_length=120)
    type            = models.IntegerField()
    samamember      = models.ForeignKey(SamaMember)
    def __unicode__(self):
        return '%s'%(self.name)

class CourseType(models.Model):
    name            = models.CharField(max_length=120)
    type            = models.IntegerField()
    def __str__(self):
        return '%s'%(self.name)

class Course(models.Model):
    #course_dates    = models.ManyToManyField(Date)
    #publication_date   = models.DateField()
    persons         = models.ManyToManyField(Person)
    types           = models.ManyToManyField(CourseType)
    locations       = models.ManyToManyField(CourseLocation)
    inscription_counter     = models.IntegerField()
    max_inscription_counter = models.IntegerField()
    status          = models.BooleanField()
    coursetype      = models.ForeignKey(CourseType)

class Participant(models.Model):
    first_name      = models.CharField(max_length=70)
    last_name       = models.CharField(max_length=70)
    birth_date      = models.DateField()
    sex             = models.IntegerField()
    email           = models.EmailField()
    address         = models.CharField(max_length=120)
    npa             = models.IntegerField()
    city            = models.CharField(max_length=50)
    phone           = models.CharField(max_length=30)
    course          = models.ForeignKey(Course)
    uuid_field      = UUIDField()
    def __unicode__(self):
        return '%s %s'%(self.first_name, self.last_name)

class Date(models.Model):
    date            = models.DateTimeField()
    course          = model.ForeignKey(Course)
    def __str__(self):
        return 'De %s a %s'%(self.date)
