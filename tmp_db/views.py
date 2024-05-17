from django.shortcuts import render

# Create your views here.
# tmp_db/views.py
from django.http import JsonResponse, HttpResponse
from .db_utils import execute_sql

def run_sql(request):
    if request.method == 'POST':
        raw_sql = request.POST.get('sql')

        # 调用db_utils.py中的execute_sql函数
        result = execute_sql(raw_sql)

        return JsonResponse(result)
    elif request.method == 'GET':
        return HttpResponse("sql测试页面")

    return JsonResponse({"status": "error", "message": "Only POST method is supported"}, status=405)
