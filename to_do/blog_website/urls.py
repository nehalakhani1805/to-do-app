"""blog_website URL Configuration

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
from django.conf.urls import include
from users import views as users_views
from django.contrib.auth import views as auth_views
from users.views import TaskUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appone.urls')),
    path('register/',users_views.register, name='register'),
    path('tasks/',users_views.tasks, name='tasks'),
    path('tasks/<int:id>/cross',users_views.cross, name='cross'),
    path('tasks/<int:id>/delete',users_views.delete, name='delete'),
    path('tasks/<int:id>/edit',users_views.edit, name='edit'),
    #path('tasks/<int:pk>/edit',TaskUpdateView.as_view(), name='edit'),
    path('profile/',users_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
