from django.conf.urls.defaults import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'getSites.*$', getSites),
    url(r'doFDC', doFDC),
    url(r'.*$', index)
)
