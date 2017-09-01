from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create', views.posts_create),
    url(r'^(?P<pk>[0-9]+)', views.posts_detail, name='detail'),
    url(r'^list', views.posts_list, name='list'),
    url(r'^update/(?P<pk>[0-9]+)', views.posts_update, name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)', views.posts_delete, name='delete'),
]




