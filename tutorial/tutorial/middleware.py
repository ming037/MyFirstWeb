# -*- coding: utf-8 -*-
#서버와 클라이언트 사이에 있는게 middleware이다.
#views.py 에서 decorator을 이용하여 하나하나 차단하는 것보다 middleware을 이용하여 한 파일에서 처리하는게 더 낫다.
import re #regular expressions
from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs): #documentation 참고 할 것
        assert hasattr(request, 'user') #user가 있는지 doublecheck
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated():
            if not any(url.match(path) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
