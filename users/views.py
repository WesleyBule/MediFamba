from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from appointments.models import Appointment
from .forms import UserRegisterForm 
from .models import Doctor , Patient 



def root_redirect(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'doctor'):
            return redirect("home_doctor")
        if hasattr(user, 'patient'):
            return redirect("home_patient")
        return redirect("home_user")
    return redirect('logIn')

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
            return redirect('home_user')
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
def home_user(request):
    return render(request, "users/home_user.html")

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
    doctor = Doctor.objects.get(user=request.user)

    appointments = Appointment.objects.filter(doctor=doctor).order_by('id')
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


@has_role_decorator('patient')
@login_required(login_url='logIn')
def agendaList(request):
    patient = Patient.objects.get(user=request.user)
    agenda = Appointment.objects.filter(patient=patient)
    context = {
        'agenda':agenda,
    }
    return render(request, "users/patients_agenda.html", context)



@has_role_decorator('patient')
@login_required(login_url='logIn')
def doctorList(request):
    doctors = Doctor.objects.all()
    doctors_lenght = Doctor.objects.count()
    context = {
        'doctors':doctors,
        'doctors_len':doctors_lenght,
    }
    
    return render(request,"users/patient_doctors.html", context)


def bookAppointment(request):
    patient = Patient.objects.get(user=request.user)
    return render(request, "users/patient_bookAppointment.html")
