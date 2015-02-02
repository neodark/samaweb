from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'samaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^section/$', views.section, name='section'),
    url(r'^faq/$', views.faq, name='faq'),
)
