from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^login$', views.login),
    url(r'^register', views.register),
    url(r'^(?P<user_id>\d+)$', views.show),  # Shows user-related info
    url(r'^$', views.index),
]
