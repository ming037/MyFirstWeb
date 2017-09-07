# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
#admin.site.register(UserProfile)
#admin.site.site_header = 'Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city','phone', 'website' )
    #user_info 대신에 description 이라고 하면 model에서 description을 찾아서 리턴해 주지만, user_info은 없기 때문에 아래에 함수로 정의한다.

    def user_info(self, obj):
        return obj.description #각 컬럼마다 표시가 된다.
    user_info.short_description = 'Info'  #테이블에 표시되는 이름을 user_info에서 Info로 바꿈

    def get_queryset(self, request): # ModelAdmin에 있는 함수 override, 데이터 정렬 할 수 있다.
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user') # ('-phone')으로 하면 내림차순으로 정렬, 폰번호 같으면 user이름으로 정렬
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)
