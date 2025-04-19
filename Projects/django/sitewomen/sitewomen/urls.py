"""
URL configuration for sitewomen project.

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
from django.urls import path, include, re_path
from women import views
from women.views import page_not_found

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name='archive'),
]

handler404 = page_not_found