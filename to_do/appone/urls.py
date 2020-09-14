from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='appone-home'),
    path('about/',views.about, name='appone-about')
]