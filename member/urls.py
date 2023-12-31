# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:31:49 2023

@author: KITCOOP
"""
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),  # member/index   ---> views.index :service method
    path("join/", views.join, name="join"), 
    path("login/", views.login, name="login"), 
    path("info/<str:id>/", views.info, name="info"), 
    path("update/<str:id>/", views.update, name="update"), 
    path("delete/<str:id>/", views.delete, name="delete"), 
    path("logout/", views.logout, name="logout"), 
    path("list/", views.list, name="list"), 
    path("passchg/", views.passchg, name="pathchg"), 
    ]












