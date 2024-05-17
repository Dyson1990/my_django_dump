from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
# 使用Django内置函数获取CSRF token
from django.middleware.csrf import get_token

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'core/home.html')
    
# core/views.py
@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')  # 假设登录后重定向到首页，你需要在urls.py中定义这个命名空间
        else:
            messages.error(request, '用户名或密码错误。')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('core:login')  # 登出后重定向回登录页面