from django.conf.urls import patterns, include, url
from . import views


partial_patterns = [
    url(
        r'^courseInfo/$',
        views.PartialGroupView.as_view(template_name='samacore/partials/courseInfo.html'),
        name='course_info',
        ),
    url(r'^(?P<template_name>[a-zA-Z_]+\.html)$', views.PartialGroupView.as_view()),
]


urlpatterns = [
    # Examples:
    # url(r'^$', 'samaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^partials/', include(partial_patterns, namespace='partials')),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^section/$', views.section, name='section'),
    url(r'^cours/$', views.courses, name='courses'),
    url(r'^specific_cours/$', views.course, name='course'),
    url(r'^faq/$', views.faq, name='faq'),
]
