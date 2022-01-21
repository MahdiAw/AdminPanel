"""Aquatricty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views
from Authentication import views as Authview

urlpatterns = [
    path('database/', admin.site.urls),
    path('admin/', include('Authentication.urls')),
    path('', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('features/', views.features,name='features'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('<int:ref>/',views.home),
    path('links/',Authview.links,name='links'),
    path('ip_table/',Authview.ip_table,name='ip_table'),
    path('map/',Authview.map,name='map'),
    path('emails/',Authview.email,name='emails'),



]
