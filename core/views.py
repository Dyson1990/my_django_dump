from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
# 使用Django内置函数获取CSRF token
from django.middleware.csrf import get_token

def home(request):

    return render(request, 'core/home.html')
    
# core/views.py
@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"csrftoken": csrf_token})


