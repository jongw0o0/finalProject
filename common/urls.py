# from django.contrib.auth import views as auth_views
# from django.urls import path

# app_name = 'common'

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_nameS='common/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]

from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'tourresult'

urlpatterns = [
    path('', views.common),
]