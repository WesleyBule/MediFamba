from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm 



def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request , 'Account created for ' +username)
            return redirect('logIn')
    context = {'form':form}
    return render(request, "users/signUp.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else :
            messages.info(request, "Invalid Email or Password")
            return render(request, 'users/logIn.html')
    context = {}
    return render(request , "users/logIn.html", context)


def home(request):
    return render(request, "users/home.html")