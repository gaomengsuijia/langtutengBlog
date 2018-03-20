#coding:utf-8
__author__ = "langtuteng"

def user_id(request):
    '''
    上下文，返回session
    :param request:
    :return:
    '''
    return {"user_id":request.session.get("userid")}