from django.conf.urls import patterns, include, url

# Class based API views
from api.views import SamaMemberList, SamaMemberDetail
from api.views import CourseTypeList, CourseTypeDetail

urlpatterns = patterns('',

    # Regular URLs
	# url(r'^samamembers/$', samamember_list, name='samamember_list'),
    # url(r'^samamembers/(?P<pk>[0-9]+)$', samamember_detail, name='samamember_detail'),

    # Class based URLs,
    url( r'^samamembers/$', SamaMemberList.as_view(), name = 'samamember_list' ),
    url( r'^samamembers/(?P<pk>[0-9]+)$', SamaMemberDetail.as_view(), name = 'samamember_detail' ),
    url( r'^coursetype/$', CourseTypeList.as_view(), name = 'coursetype_list' ),
    url( r'^coursetype/(?P<pk>[0-9]+)$', CourseTypeDetail.as_view(), name = 'coursetype_detail' ),
)
