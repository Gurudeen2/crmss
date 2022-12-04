from django.urls import path 
from .views import *


urlpatterns=[
    path('', index, name='crime' ),
    path('<int:crimeid>', viewcrime, name='view' ),
    path('addcrime', addcrime, name='addcrime'),
    path("delete", deletecrime, name="delete")
]