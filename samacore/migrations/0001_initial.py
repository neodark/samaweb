# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=300)),
                ('inscription_counter', models.IntegerField()),
                ('max_inscription_counter', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('type', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('course', models.ForeignKey(to='samacore.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('birth_date', models.DateField()),
                ('sex', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=120)),
                ('npa', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('uuid_field', django_extensions.db.fields.UUIDField(editable=False, blank=True)),
                ('course', models.ForeignKey(to='samacore.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamaGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('type', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SamaMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('birth_date', models.DateField()),
                ('sex', models.IntegerField()),
                ('email', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=120)),
                ('npa', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='samagroup',
            name='samamember',
            field=models.ForeignKey(to='samacore.SamaMember'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coursetype',
            field=models.ForeignKey(to='samacore.CourseType'),
            preserve_default=True,
        ),
    ]
