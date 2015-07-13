# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

__author__ = 'mayns'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.get_data, name='get_data'),
    url(r'^(?P<swot_id>[0-9]*)$', views.modify, name='modify'),
]