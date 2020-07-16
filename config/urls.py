"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from notice import views as notice_views

urlpatterns = [
    path('f/admin/', admin.site.urls),
    path('f/list/', notice_views.notice_list, name='f_notice_list'),
    path('f/create/', notice_views.notice_create, name='f_notice_create'),
    path('f/update/<int:pk>/', notice_views.notice_update, name='f_notice_update'),
    path('f/<int:pk>/', notice_views.notice_detail, name='f_notice_detail'),
    path('f/delete/<int:pk>/', notice_views.notice_delete, name='f_notice_delete'),


    path('c/list/', notice_views.NoticeListView.as_view(), name='c_notice_list'),
    path('c/create/', notice_views.NoticeCreateView.as_view(), name='c_notice_create'),
    path('c/update/<int:pk>/', notice_views.NoticeUpdateView.as_view(), name='c_notice_update'),
    path('c/<int:pk>/', notice_views.NoticeDetailView.as_view(), name='c_notice_detail'),
    path('c/delete/<int:pk>/', notice_views.NoticeDeleteView.as_view(), name='c_notice_delete'),
]
