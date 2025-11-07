from django.shortcuts import render , redirect
from .models import Patient

from .forms import UserRegisterForm

def user_register(request):
    form = UserRegisterForm
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('#')
    context = {'form':form}
    return render(request, "users/signin.html", context)