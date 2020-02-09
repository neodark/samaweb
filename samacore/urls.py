from django.conf.urls import include, url
from . import views

app_name = 'samacore'
partial_patterns = [
    url(
        r'^courseInfo/$',
        views.PartialGroupView.as_view(template_name='samacore/partials/courseInfo.html'),
        name='course_info',
        ),
    url(
        r'^courseInfoAdmin/$',
        views.PartialGroupView.as_view(template_name='samacore/partials/courseInfoAdmin.html'),
        name='course_info_admin',
        ),
    url(
        r'^courseRegistration/$',
        views.PartialGroupView.as_view(template_name='samacore/partials/courseRegistration.html'),
        name='course_registration',
        ),
    url(
        r'^courseEditParticipant/$',
        views.PartialGroupView.as_view(template_name='samacore/partials/courseEditParticipant.html'),
        name='course_participant_edition',
        ),
    url(r'^(?P<template_name>[a-zA-Z_]+\.html)$', views.PartialGroupView.as_view()),
]


urlpatterns = [
    # Examples:
    # url(r'^$', 'samaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^partials/', include(partial_patterns, namespace='partials')),
    url(r'^partials/', include((partial_patterns, "samacore"), namespace='partials')),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^section/$', views.section, name='section'),
    url(r'^cours/$', views.courses, name='courses'),
    url(r'^specific_cours/$', views.course, name='course'),
    url(r'^register_cours/$', views.register_course, name='register_course'),
    url(r'^add_cours/$', views.add_course, name='add_course'),
    url(r'^edit_cours/$', views.edit_course, name='edit_course'),
    url(r'^archive_cours/$', views.archive_course, name='archive_course'),
    url(r'^participants_cours/$', views.participants_course, name='participants_course'),
    url(r'^participant_cours_edit/$', views.participant_course_edit, name='participant_course_edit'),
    url(r'^participant_cours_delete/$', views.participant_course_delete, name='participant_course_delete'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^membres/$', views.membres, name='membres'),
    url(r'^add_program/$', views.add_program, name='add_program'),
    url(r'^edit_program/$', views.edit_program, name='edit_program'),
    url(r'^admin_login/$', views.admin_login, name='admin_login'),
]
