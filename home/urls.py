from .views import home_page , Term_1 , Terms , Term_2 , Term_3
from django.urls import path 

urlpatterns = [
    path('',home_page.as_view() , name="home_page" ),
    path('term/' , Terms.as_view() , name = 'terms'),
    path('term/1' , Term_1.as_view() , name= "term-1"),
    path('term/2' , Term_2.as_view() , name = 'term-2'),
    path('term/3' , Term_3.as_view() , name = 'term-3')

]
