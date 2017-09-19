from django.conf.urls import url
from home.views import HomeView #from home import views
from . import views
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'), #url(r'^$', views.home, name='home')  class based view
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')

]
