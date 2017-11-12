from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<game_id>\d+)/home$', views.home),
    url(r'^(?P<game_id>\d+)/diffuse$', views.diffuse),
    url(r'^(?P<game_id>\d+)/history$', views.history),
    url(r'^getgame$', views.gotogame),
]
