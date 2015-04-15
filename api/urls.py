from django.conf.urls import patterns, include, url

# Rest framework
from rest_framework import routers
# Class based API views
from api.views import SamaMemberList, SamaMemberDetail
from api.views import SamaGroupList, SamaGroupDetail
from api.views import ParticipantList, ParticipantDetail
from api.views import CourseList, CourseDetail
from api.views import CourseTypeList, CourseTypeDetail
from api.views import DateList, DateDetail

router = routers.SimpleRouter()

urlpatterns = patterns('',

    # Regular URLs
	# url(r'^samamembers/$', samamember_list, name='samamember_list'),
    # url(r'^samamembers/(?P<pk>[0-9]+)$', samamember_detail, name='samamember_detail'),

    # Class based URLs,
    url( r'^samamembers/$', SamaMemberList.as_view(), name = 'samamember_list' ),
    url( r'^samamembers/(?P<pk>[0-9]+)$', SamaMemberDetail.as_view(), name = 'samamember_detail' ),
    url( r'^samagroup/$', SamaGroupList.as_view(), name = 'samagroup_list' ),
    url( r'^samagroup/(?P<pk>[0-9]+)$', SamaGroupDetail.as_view(), name = 'samagroup_detail' ),
    url( r'^participants/$', ParticipantList.as_view(), name = 'participant_list' ),
    url( r'^participants/(?P<pk>[0-9]+)$', ParticipantDetail.as_view(), name = 'participant_detail' ),
    url( r'^date/$', DateList.as_view(), name = '_date_list' ),
    url( r'^date/(?P<pk>[0-9]+)$', DateDetail.as_view(), name = '_date_detail' ),
    url( r'^course/$', CourseList.as_view(), name = 'course_list' ),
    url( r'^course/(?P<pk>[0-9]+)$', CourseDetail.as_view(), name = 'course_detail' ),
    url( r'^coursetype/$', CourseTypeList.as_view(), name = 'coursetype_list' ),
    url( r'^coursetype/(?P<pk>[0-9]+)$', CourseTypeDetail.as_view(), name = 'coursetype_detail' ),
    url( r'^', include(router.urls) ),
)