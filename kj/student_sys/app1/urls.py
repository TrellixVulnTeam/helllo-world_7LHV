"""student_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('st/', views.show_st, name='st'),
    path('show_login/', views.show_login, name='sl'),
    path('login_data/', views.login_data, name='login_data'),
    path('show_regist/', views.show_regist, name='sr'),
    path('regist_account/', views.regist_account, name='regist_account'),
    path('show_upload/', views.render_upload, name='upload'),
    path('deal_file/<str:account>/', views.deal_file, name='deal_file'),
]
