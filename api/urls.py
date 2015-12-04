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
from api.views import CourseCreationNewView, CourseDetailView
from api.views import ParticipantNewCreationView, ParticipantDetailView
from api.views import UserView
from api.views import AuthView

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
    url( r'^coursenew/$', CourseCreationNewView.as_view(), name = 'coursenew_list' ),
    url( r'^coursenew/(?P<pk>[0-9]+)$', CourseDetailView.as_view(), name = 'coursenew_detail' ),
    url( r'^participantnew/$', ParticipantNewCreationView.as_view(), name = 'paticipantnew_list' ),
    url( r'^participantnew/(?P<pk>[0-9]+)$', ParticipantDetailView.as_view(), name = 'participantnew_detail' ),
    url( r'^coursetype/$', CourseTypeList.as_view(), name = 'coursetype_list' ),
    url( r'^coursetype/(?P<pk>[0-9]+)$', CourseTypeDetail.as_view(), name = 'coursetype_detail' ),
    url(r'^accounts/$', UserView.as_view('list')),
    url(r'^auth/$', AuthView.as_view(), name='authenticate'),
    url( r'^', include(router.urls) ),
)
