"""
URL configuration for auctionProject project.

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
from auctionsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashbord),
    path('admin_login',views.admin_login),
    path('admin_control_page/',views.admin_control_page),
    path('do_admin_login/',views.do_admin_login),
    path('admin_log_out/',views.admin_log_out),
    path('register_user/',views.register_user),
    path('save_new_user/',views.save_new_user),
    path('login_user/',views.login_user),
    path('do_login/',views.do_login),
    path('dashbord/',views.dashbord),
    path('log_out/',views.log_out),
    path('edit_user/',views.edit_user),
    path('update_user/',views.update_user),
    path('delete_user/',views.delete_user),
    path('user_list/',views.user_list),
    path('auction/',views.auction),
    path('save_product/',views.save_product),
    path('biditem/',views.biditem),
    path('validate/',views.validate)
]
