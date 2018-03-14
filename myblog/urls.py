#coding:utf-8
__author__ = "langtuteng"
from django.conf.urls import include, url
from myblog import views_api

urlpatterns = [
    url(r'^thumb/(\d+)$',views_api.thumb,name="thumb"),
    url(r'^login$',views_api.login,name="login"),
    ]