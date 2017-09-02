# -*- coding: utf-8 -*-
#서버와 클라이언트 사이에 있는게 middleware이다.
#views.py 에서 decorator을 이용하여 하나하나 차단하는 것보다 middleware을 이용하여 한 파일에서 처리하는게 더 낫다.
import re #regular expressions
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

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

        # if not request.user.is_authenticated(): # logout 하면 특정 페이지들 접근 못하도록.
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == 'account/logout/':  #이게 없으면 로그아웃이 안 됨.
            logout(request)

        if request.user.is_authenticated() and url_is_exempt:  #login 이미 했으면 login이나 register에 접근할 수 없다.
            return redirect(settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated() or url_is_exempt: #login 되어있는데 url이 exempt 아닌 경우, 반대 경우도 해당
            return None
        else: #login 안 되었을 경우
            return redirect(settings.LOGIN_URL)
