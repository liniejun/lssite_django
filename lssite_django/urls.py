"""lssite_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include
import tutorial.views
from login import views

# 登录界面路由设计
# /home  home.html  主页
# /login login.html 登录
# /logout 无需页面 登出
# /register register.html 注册
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',tutorial.views.index),
    path('polls/', include('polls.urls')),
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
]
