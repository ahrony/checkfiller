from django.conf.urls import patterns, include, url
from check import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fillme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.add_new, name='new'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^test/$', views.test, name='test'),


)
