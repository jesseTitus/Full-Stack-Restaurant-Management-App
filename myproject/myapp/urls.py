from django.urls import path, include, re_path
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('menu/', views.menu, name="menu"),
        path('about/', views.about, name="about"),
        path('book/', views.Book.as_view(), name="book"),
        path('form/', views.form, name="form"),
        path('modelform/', views.modelform, name="modelform"),
        re_path(r'^menu$', views.menu, name='menu_no_slash'), #make trailing slash optional 
] 