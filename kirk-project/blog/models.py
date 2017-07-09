#-*- coding: utf-8 -*-

from __future__ import unicode_literals  # 문자열 처리
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    # slug 컬럼은 제목의 별칭
    # SlugFiled에 unique 옵션을 추가해 특정 포스트를 검색시 기본키 대신 사용
    # allow_unicode -> 한글 사용 가능
    # help_text는 해당 컬럼을 설명해주는 문구를 폼 화면에 나타냄
    slug = models.SlugField('Slug', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    # TextFeild는 여러줄 입력이 가능
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modfiy Date', auto_now=True)

    # 필드 속성외에 필요한 파라미터가 있으면 Meta 내부 클래스로 정의 한다
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # 데이터베이스에 저장되는 테이블 이름을 'my_post'로 지정
        db_table = 'my_post'
        # 모델 객체의 리스트 출력시 modify_date 컬럼을 기준으로 내림차순으로 정렬
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    # 이 메소드가 정의된 객체를 지정하는 URL을 반환. 메소드 내에서는 장고의 내장함수인 reverse()를 호출
    def get_absoulte_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # modify_date 컬럼을 기준으로 이전 포스트를 반환,
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # modify_date 컬럼을 기준으로 다음 포스트를 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()