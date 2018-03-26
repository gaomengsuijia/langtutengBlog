#coding:utf-8
__author__ = "langtuteng"

from django import forms

class Article_form(forms.Form):
    '''
    发帖的表单
    '''
    title = forms.CharField(max_length=255,min_length=1)
    head_img = forms.ImageField()
    content = forms.CharField(max_length=25555,min_length=2)
    categroy = forms.IntegerField()
    summary = forms.CharField(max_length=255,min_length=2)
    author = forms.IntegerField()
