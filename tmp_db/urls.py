# tmp_db/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sql/', views.run_sql, name='run_sql'),
]
