#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Brief
# @Version 1.0
# @Date
#
#
__author__ = 'Shawn Lee'

from . import views
from django.urls import path

urlpatterns =[
    path('', views.index, name='index'),
]
