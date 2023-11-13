"""
URL configuration for API project.

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

    re_path('login', auth_views.login),
    re_path('signup', auth_views.signup),
    re_path('test_token', auth_views.test_token),
    super user password : ali
"""
from django.contrib import admin
from ClincApp.api import auth_views
from django.urls import path
from django.views.generic import TemplateView
from django.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'api/', include('ClincApp.urls')),
    path('api-token-auth', auth_views.obtain_auth_token),
    path('test-front-end', TemplateView.as_view(template_name = "index.html"))
]
