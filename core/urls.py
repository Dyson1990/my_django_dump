# my_django/core/urls.py

from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('csrf-token/', views.get_csrf_token, name='get_csrf_token'),

]
