#coding:utf-8
__author__ = "langtuteng"
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from myblog.models import Article,Categroy,Fangjia
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    '''
    登录,post
    :param request:
    :return:
    '''
    pass





@login_required
def thumb(request,id):
    '''
    点赞
    :param request:
    :return:
    '''
    return JsonResponse({"info":"ok"})