from django.urls import path
from .views import *
urlpatterns=[
    path('', index, name="criminalindex"),
    path("add", criminaladd, name="criminaladd"),
    path("search", search, name="search")
]