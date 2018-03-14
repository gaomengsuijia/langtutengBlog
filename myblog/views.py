from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import json
from myblog.models import Article,Categroy,Fangjia
# Create your views here.


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
    #查询文章
    articles = Article.objects.filter(hidden=0)

    #查询版块
    categroys = Categroy.objects.all()
    print(articles)
    return render(request,'index.html',{'articles':articles,'categroys':categroys})