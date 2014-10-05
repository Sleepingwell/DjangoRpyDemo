from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    url(r'getSites.*$', getSites),
    url(r'doFDC', doFDC),
    url(r'.*$', index)
)
