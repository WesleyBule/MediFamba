from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

from appointments.models import Appointment
from .forms import UserRegisterForm 
from .models import Doctor , Patient 


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
            

            if Doctor.objects.filter(user=user).exists():
                assign_role(user , 'doctor')
                return redirect('home_doctor')
            elif Patient.objects.filter(user=user).exists():
                assign_role(user , 'patient')
                return redirect('home_patient')
            assign_role(user, 'user')
            return redirect('home')
        else :
            messages.info(request, "Invalid Username or Password")
            return render(request, 'users/logIn.html')
    context = {}
    return render(request , "users/logIn.html", context)

def user_logout(request):
    logout(request)
    return redirect('logIn')


@has_role_decorator('user')
@login_required(login_url='logIn')
def home(request):
    return render(request, "users/home.html")

@has_role_decorator('user')
@login_required(login_url='logIn')
def information(request):
    return render(request, "users/info.html")



@has_role_decorator('doctor')
@login_required(login_url='logIn')
def home_doctor(request):
    return render(request, "users/home_doctor.html")


@has_role_decorator('doctor')
@login_required(login_url='logIn')
def appointmentList(request):
  appointments = Appointment.objects.all()
  context = {
    "appointments":appointments,
  }
  return render(request,"users/appointments.html",context)


@has_role_decorator('doctor')
@login_required(login_url='logIn')
def patientList(request):
    patients = Patient.objects.all()
    context = {
        'patients':patients,
    }
    return render(request, "users/doctor_patients.html", context)




@has_role_decorator('patient')
@login_required(login_url='logIn')
def home_patients(request):
    return render(request, "users/home_patients.html")


