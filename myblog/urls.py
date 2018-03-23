#coding:utf-8
__author__ = "langtuteng"
from django.conf.urls import include, url
from myblog import views_api

urlpatterns = [
    url(r'^thumb$',views_api.thumb,name="thumb"),
    url(r'^login_check',views_api.login_check,name="login_check"),
    url(r'^logout',views_api.logout,name="logout"),
    ]