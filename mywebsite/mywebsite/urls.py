"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from library import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.home, name='home'),
    path(r'login', views.loginadm, name='loginadm'),
    path(r'input', views.input, name='input'),
    path(r'detailbook', views.detailbook, name='detailbook'),
    path(r'logout', views.logoutadm, name="logout"),
]
