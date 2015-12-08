from django.conf.urls import patterns, include, url

# Rest framework
from rest_framework import routers
# Class based API views
from api.views import CourseCreationNewView, CourseDetailView
from api.views import ParticipantNewCreationView, ParticipantDetailView
from api.views import UserView
from api.views import AuthView

router = routers.SimpleRouter()

urlpatterns = patterns('',

    # Regular URLs

    # Class based URLs,
    url( r'^course/$', CourseCreationNewView.as_view(), name = 'course_list' ),
    url( r'^coursenew/(?P<pk>[0-9]+)$', CourseDetailView.as_view(), name = 'coursenew_detail' ),
    url( r'^participantnew/$', ParticipantNewCreationView.as_view(), name = 'paticipantnew_list' ),
    url( r'^participantnew/(?P<pk>[0-9]+)$', ParticipantDetailView.as_view(), name = 'participantnew_detail' ),
    url(r'^accounts/$', UserView.as_view('list')),
    url(r'^auth/$', AuthView.as_view(), name='authenticate'),
    url( r'^', include(router.urls) ),
)
