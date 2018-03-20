"""langtutengBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myblog import views as myblog_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', myblog_views.index),
    url(r'^$',myblog_views.index,name="index"),
    url(r'^fuli$',myblog_views.fuli,name="fuli"),
    url(r'^movie$',myblog_views.movie,name="movie"),
    url(r'^more$',myblog_views.more,name="more"),
    url(r'^fangjia$',myblog_views.fangjia,name="fangjia"),
    url(r'^article_detail/(\d+)$',myblog_views.article_detail,name="article_detail"),
    url(r'^api/',include('myblog.urls',namespace='myblog')),#命名空间,映射到下级app，myblog
    url(r'^login$',myblog_views.login,name="login"),
    ]
