from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from samacore import views

app_name = 'samaweb'
urlpatterns = [
    # Examples:
    # url(r'^$', 'samaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('samacore.urls', 'samacore')),
    #url(r'^', include('samacore.urls', namespace='samacore')),
    #url(r'^', include(('samacore.urls', 'samacore'), namespace='samacore')),
    #url(r'^section/$', samacore.views.section, name='section'),
    # Include API URLs0
    url(r'^api/', include('api.urls', 'api')),
]
urlpatterns += staticfiles_urlpatterns()
