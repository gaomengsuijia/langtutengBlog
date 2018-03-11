from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserGroup(models.Model):
    '''
    用户组
    '''
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    '''
    账户
    '''
    user = models.OneToOneField(User)#（账户表，继承django的user原始表）
    name = models.CharField(max_length=255)
    group = models.ManyToManyField("UserGroup")#一个用户可以属于多个用户组,django会自动生成一个中间表，进行关联

    def __str__(self):
        return self.name



class ThumbUp(models.Model):
    '''
    点赞
    '''
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "article=%s,user=%s"%(self.article,self.user)



class Comment(models.Model):
    '''
    文章的评论
    '''

    user = models.ForeignKey("UserProfile")
    content = models.CharField(max_length=500)
    comment_date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey("Article")
    parent_comment = models.ForeignKey('self',related_name='p_comment',blank=True,null=True)#关联自己本身，作为父级评论

    def __str__(self):
        return "user=%s,content=%s"%(self.user,self.content)



class Article(models.Model):
    '''
    文章模型
    '''

    title = models.CharField(max_length=255,unique=True)
    head_img = models.ImageField(upload_to="uploads")
    content = models.TextField(max_length=5000)
    categroy = models.ForeignKey("Categroy")#加上引号，通过映射去找该类
    summary = models.CharField(max_length=255)
    author = models.ForeignKey("UserProfile")
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField()
    priority = models.IntegerField()



    def __str__(self):
        return self.title


class Categroy(models.Model):
    '''
    版块
    '''
    name = models.CharField(max_length=255,unique=True)
    admin = models.ForeignKey("UserProfile")#版块的管理者

    def __str__(self):
        return self.name















