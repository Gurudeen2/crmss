from django.urls import path
from . import views

urlpatterns =[
    path('login', views.login, name='login'),
    path("dashboard", views.index, name="dashboard"),
    path('register', views.register, name='register'),
]