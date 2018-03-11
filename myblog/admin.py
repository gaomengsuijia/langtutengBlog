from django.contrib import admin
from myblog.models import UserGroup,ThumbUp,Article,Categroy,Comment,UserProfile
# Register your models here.

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish_date',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategroyAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(UserGroup,UserGroupAdmin)
admin.site.register(Categroy,CategroyAdmin)
admin.site.register(UserProfile,UserProfileAdmin)