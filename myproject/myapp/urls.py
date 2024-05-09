from django.urls import path, include, re_path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.home, name="home"),
        path('menu/', views.menu, name="menu"),
        path('about/', views.about, name="about"),
        path('book/', views.Book.as_view(), name="book"),
        path('form/', views.form, name="form"),
        path('modelform/', views.modelform, name="modelform"),
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Login page
        path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),  # Logout functionality
        re_path(r'^menu$', views.menu, name='menu_no_slash'), #make trailing slash optional 
        
        path('register', views.register, name="register"),
        path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] 