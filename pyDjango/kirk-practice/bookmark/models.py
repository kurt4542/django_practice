#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):    # 객체를 문자열로 표현할 때 사용하는 함수, 이 함수를 정의하지 않으면 테이블명이 제대로 표현되지 않음.
        return self.title

        #def __str__(self):
        #    return "%s %s" %(self.title, self.url)