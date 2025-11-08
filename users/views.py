from django.shortcuts import render , redirect
from .models import Patient

from .forms import UserRegisterForm 

def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logIn')
    context = {'form':form}
    return render(request, "users/signUp.html", context)


def user_login(request):
    context = {}
    return render(request , "users/logIn.html", context)


def home(request):
    return render(request, "users/home.html")