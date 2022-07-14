from re import L
from .views import Login , Logout
from django.urls import path 

urlpatterns = [
    path("login/" , Login.as_view() , name='login' ),
    path("logout/" , Logout.as_view() , name="logout"),
]
