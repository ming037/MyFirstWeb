# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='Gwangju')

class UserProfile(models.Model): #수정할 때마다 migration 해주어야 한다.
    user = models.OneToOneField(User) # add database model (python manage.py makemigrations) (python manage.py migrate)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    Gwangju = UserProfileManager()

    def __str__(self): # admin 페이지에서 user_profile 제목이 유저 이름으로 나오게 함.
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']: #connet에서 sender=User의 User가 create되면 아래 코드 실행
        user_Profile = UserProfile.objects.create(user=kwargs['instance'])
        # kwargs['instance']는 sender=User의 오브젝트이다.

#장고 오프젝트를 저장하고 post_save 시그널 후에 코드가 동작함.
post_save.connect(create_profile, sender=User)
