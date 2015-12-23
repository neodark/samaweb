from django.conf.urls import patterns, include, url

# Rest framework
from rest_framework import routers
# Class based API views
from api.views import SectionCreationNewView, SectionDetailView
from api.views import CourseCreationNewView, CourseDetailView
from api.views import ParticipantCreationView, ParticipantDetailView
from api.views import UserView
from api.views import AuthView

router = routers.SimpleRouter()

urlpatterns = patterns('',

    # Regular URLs

    # Class based URLs,
    url( r'^section/$', SectionCreationNewView.as_view(), name = 'section_list' ),
    url( r'^section/(?P<pk>[0-9]+)$', SectionDetailView.as_view(), name = 'section_detail' ),
    url( r'^course/$', CourseCreationNewView.as_view(), name = 'course_list' ),
    url( r'^course/(?P<pk>[0-9]+)$', CourseDetailView.as_view(), name = 'course_detail' ),
    url( r'^participant/$', ParticipantCreationView.as_view(), name = 'paticipant_list' ),
    url( r'^participant/(?P<pk>[0-9]+)$', ParticipantDetailView.as_view(), name = 'participant_detail' ),
    url(r'^accounts/$', UserView.as_view('list')),
    url(r'^auth/$', AuthView.as_view(), name='authenticate'),
    url( r'^', include(router.urls) ),
)
