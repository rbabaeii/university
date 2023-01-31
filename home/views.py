from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class home_page(View):
    def get(self ,request):
        return render(request , "home/index.html")

# @method_decorator(login_required(login_url="login" ), name="dispatch")
# class Nomre(View):
#     def get(self , request):
#         return render(request , "home/nomreh.html")

class Terms(View):
    def get(self , request):
        return render(request , 'home/term.html')

@method_decorator(login_required(login_url="login" ), name="dispatch")
class Term_1(View):
    def get(self , request):
        return render(request , 'home/nomreh1.html')


@method_decorator(login_required(login_url="login" ), name="dispatch")
class Term_2(View):
    def get(self , request):
        return render(request , 'home/nomreh2.html')


@method_decorator(login_required(login_url="login" ), name="dispatch")
class Term_3(View):
    def get(self , request):
        return render(request , 'home/nomreh3.html')