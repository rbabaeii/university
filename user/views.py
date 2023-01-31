import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User

# Create your views here.
class Login(View):
    def get(self , request):
        return render(request,"user/account.html")
    def post(self , request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user:
            login(request,user)
            return redirect('nomre')
        else:
            return HttpResponse("نام کاربری یا رمز عبور اشتباه میباشد لطفا دوباره تلاش کنید")
class Logout(View):
    def get(self , request):
        logout(request)
        return redirect("home_page")