from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from samacore import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'samaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('samacore.urls')),
    #url(r'^section/$', samacore.views.section, name='section'),

    # Include API URLs
	url(r'^api/', include('api.urls')),

)
urlpatterns += staticfiles_urlpatterns()
