from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import json
# Create your views here.

def index(request):
    return render(request,'index.html')

def redic(request):
    return render(request,'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # return render(request,'index.html',{'username':username,'password':password})
        return JsonResponse({'username':username,'password':password})
    else:
        return HttpResponse("bad")
    

def xiecheng(request):
    return render(request,'index.html')