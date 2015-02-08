from django.db import models

# Create your models here.

#class Participant(models.Model):
#    first_name = models.CharField(max_length=70)
#    last_name = models.CharField(max_length=70)
#    birth_date = models.DateField()
#    sex = models.IntegerField()
#    email = models.EmailField()
#    address = models.CharField(max_length=120)
#    npa = models.IntegerField()
#    city = models.CharField(max_length=50)
#    phone = models.CharField(max_length=30)
#    def __unicode__(self):
#        return '%s %s'%(self.first_name, self.last_name)
#
#class SamaMember(models.Model):
#    first_name = models.CharField(max_length=70)
#    last_name = models.CharField(max_length=70)
#    birth_date = models.DateField()
#    sex = models.IntegerField()
#    email = models.EmailField()
#    address = models.CharField(max_length=120)
#    npa = models.IntegerField()
#    city = models.CharField(max_length=50)
#    phone = models.CharField(max_length=30)
#    types = models.ManyToManyField(PersonType)
#    ranks = models.ManyToManyField(PersonRank)
#    headshot = models.ImageField(upload_to='/tmp')
#    def __unicode__(self):
#        return '%s %s'%(self.first_name, self.last_name)
