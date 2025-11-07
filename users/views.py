from django.shortcuts import render , redirect
from .models import Patient

from .forms import UserRegisterForm

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, "users/signin.html", context)