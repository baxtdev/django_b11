from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('register/', accounts_views.register_view, name='register'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
]
