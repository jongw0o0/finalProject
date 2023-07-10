"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from mainpage.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # mainpage
    path('common/', include('common.urls')),
    path('savearea/', include('savearea.urls')),
    path('tourlist/', include('tourlist.urls')),
    path('classification/', include('classification.urls')),
    path('tourselect/', include('tourselect.urls')),
    # path('tourresult/', include('tourresult.urls')),
    path('tourdetail/', include('tourresult.urls')),  # tourdetail 안에서 상세페이지 나누기







    # path('signup', views.signup),
    # path('login', views.login),
]
