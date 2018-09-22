from django.shortcuts import render, redirect  # 导入重定向
from django.contrib.auth import authenticate, login, logout  # 导入内置登陆退出方法
from django.contrib.auth.decorators import login_required


def bds_login(request):
    if request.method == 'GET':
        return render(request, "bds_main/login.html")  # 用login.html来显示
    else:
        username = request.POST['inputeid']
        password = request.POST['inputpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("bds_main/")
        else:
            return render(request, "bds_main/login.html", {'errorMsg': '用户名或密码错误，请重试！'})


@login_required
def bds_main(request):
    return render(request, "bds_main/main.html")


@login_required
def bds_logout(request):
    logout(request)
    return render(request, "bds_main/login.html")
