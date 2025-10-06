from django.views import View
from django.shortcuts import render, redirect
from .form import SignUpForm
from .models import CustomUser

# Create your views here.

class home_view(View):

    def get(self, request):

        return render(request, "Home/profile.html")

class register_view(View):

    def get(self, request):

        form = SignUpForm()

        return render(request, "login/register.html", {"form": form})
    
    def post(self, request):

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password1")

        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        return redirect("login")    
    


    