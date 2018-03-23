from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import json
from myblog.models import Article,Categroy,Fangjia
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    '''
    登录页面
    :param request:
    :return:
    '''
    return render(request,"login.html")



def article_detail(request,article_id):
    '''
    文章详情
    :param request:
    :return:
    '''
    try:
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        # raise ObjectDoesNotExist("对象不存在")
        return render(request,"404.html")
    return render(request,"article_detail.html",{"article":article})

def fangjia(request):
    '''
    房价排行
    :param request:
    :return:
    '''
    fanjia = Fangjia.objects.all()
    print(fanjia)
    data = []
    for each in fanjia:
        info = {}
        info["cityname"] = each.cityname
        info["sara"] = each.sara
        info["fanjia"] = each.fanjia
        info["bili"] = each.bili
        data.append(info)
    return render(request,"fangjia.html",{"data":json.dumps(data)})
    # return render(request, "fangjia.html")
def more(request):
    '''
    更多
    :param request:
    :return:
    '''
    return render(request,'more.html')

def movie(request):
    '''
    电影版块
    :param request:
    :return:
    '''
    return render(request,'movie.html')

@login_required
def fuli(request):
    '''
    福利版块
    :param request:
    :return:
    '''
    return render(request,'fuli.html')


def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    #查询普通文章，按权重倒序排列
    articles = Article.objects.filter(hidden=0 ,hot=0).order_by("-priority")
    #查询热点文章，按权重倒序排列
    hot_articles = Article.objects.filter(hidden=0,hot=1).order_by("-priority")
    #查询版块
    categroys = Categroy.objects.all()
    print(articles)
    #查询文章的点赞数
    return render(request,'index.html',{'articles':articles,'categroys':categroys,'hot_articles':hot_articles})