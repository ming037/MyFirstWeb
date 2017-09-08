from django.conf.urls import url
from home.views import HomeView #from home import views
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home') #url(r'^$', views.home, name='home')
]
