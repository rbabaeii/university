from tkinter import N
from turtle import home
from .views import home_page , Nomre
from django.urls import path 

urlpatterns = [
    path('',home_page.as_view() , name="home_page" ),
    path('nomreh/' , Nomre.as_view() , name= "nomre"),
]
