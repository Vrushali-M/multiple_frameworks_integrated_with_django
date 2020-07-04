"""mysite URL Configuration

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

from django.views.generic import TemplateView

#main website
from personal.views import (
    about_page,
)

#to do app views
from todo.views import (
    todo_app,
    task_list,
    task_detail,
    task_create,
    task_update,
    task_delete,
    todo_app,
    manifest,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', todo_app, name = "urls"),

    #main website links
    path('about/', about_page, name="about"),

    #todo list website with react
    path('todo/', task_list, name = 'task_list' ),
    path('todo/detail/<str:pk>', task_detail, name = 'task_detail' ),
    path('todo/create/', task_create, name = 'task_create' ),
    path('todo/update/<str:pk>', task_update, name = 'task_update' ),
    path('todo/delete/<str:pk>', task_delete, name = 'task_delete' ),
    path('todo_r/', TemplateView.as_view(template_name = 'index.html')),

    

]
