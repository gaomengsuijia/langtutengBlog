#coding:utf-8
__author__ = "langtuteng"
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from myblog.models import Article,Categroy,Fangjia,UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_check(request):
    '''
    登录,post
    :param request:
    :return:
    '''
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            return JsonResponse({"code":4001,"info":"username or password is null"})
        else:
            try:
                user = UserProfile.objects.get(username=username,password=password)
                print(username, password)
                request.session["userid"] = {"userid":user.id,"name":user.name}#添加session
                return JsonResponse({"code": 2001, "info": "login success"})
            except Exception as e:
                return JsonResponse({"code": 4001, "info": "username or password erro"})
    else:
        return JsonResponse({"code":5001,"info":"method erro"})



def logout(request):
    '''
    退出登录
    :param request:
    :return:
    '''
    try:
        del request.session["userid"]
    except KeyError as e:
        pass
    return JsonResponse({"code":2001,"info":"logout sucess"})


@login_required
def thumb(request,id):
    '''
    点赞
    :param request:
    :return:
    '''
    return JsonResponse({"info":"ok"})