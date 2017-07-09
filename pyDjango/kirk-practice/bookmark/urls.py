#-*- coding: utf-8 -*-

from django.conf.urls import url
from .views import BookmarkLV, BookmarkDV

urlpatterns = [
    # Class-based views for Bookmark app
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]