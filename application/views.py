from django.shortcuts import render,HttpResponse
import json

# Create your views here.
def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == "POST":
        # 初始化返回值
        res = {"code":200,"data":None,"error":None}

        user = request.POST.get('username')
        pwd = request.POST.get('password')
        # 判断用户名和密码

        if user == 'xiao' and pwd == '1234':
            print("登录成功")
        else:
            res['code'] = 500
            res['error'] = "用户名或密码错误"

        return HttpResponse(json.dumps(res))


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse("欢迎回来")