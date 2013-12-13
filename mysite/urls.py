from django.conf.urls import patterns, include, url
from mysite.views import home, current_datetime, paint, save, gallery, load, about

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^about/$',about),
    url(r'^time/$',current_datetime),
    url(r'^paint/$',paint),
    url(r'^save/$', save),
    url(r'^gallery/$', gallery),
    url(r'^gallery/([^/]+)$', load),
)


