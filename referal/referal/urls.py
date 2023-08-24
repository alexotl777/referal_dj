"""
URL configuration for referal project.

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
from django.urls import path
from authentication.views import *
from sms_code.views import *
from MyProfile.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authAPI.as_view()),
    path('code/', authAPI.code, name='code'),
    path('user_profile/', viewProfile.as_view(), name='user_profile'),
]
