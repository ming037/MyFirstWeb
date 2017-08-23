from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name':'accounts/login.html'})
    #두 번째 인자는 view, 마지막 인자는 render용 템플릿
]
