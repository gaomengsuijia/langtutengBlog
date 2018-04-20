#coding:utf-8
__author__ = "langtuteng"
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from myblog.models import Article,Categroy,Fangjia,UserProfile,ThumbUp
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def register_check(request):
    '''
    注册,post
    :param request:
    :return:
    '''
    pass


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
                return JsonResponse({"code": 2001, "info": "login success","userid":user.id})
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
def thumb(request):
    '''
    点赞
    :param request:
    :return:
    '''
    if request.method == "POST":
        arid = request.POST["arid"]
        userid = request.POST["userid"]

        print(arid, userid)
        if arid == "" or userid == "":
            return JsonResponse({"info":"para is null"})

        tb_exit = ThumbUp.objects.filter(article=arid,user=userid)

        if tb_exit:
            return JsonResponse({"code": 1})  # code=1,已点赞

        #插入点赞表
        try:
            arti = Article.objects.get(id=arid)
            user = UserProfile.objects.get(id=userid)
            tb = ThumbUp(article=arti,user=user)
            tb.save()
            return JsonResponse({"code": 0})#code=0,点赞成功
        except Exception as e:
            print(str(e))
            raise Exception("插入失败")


    else:
        return JsonResponse({"info":"erro type"})
