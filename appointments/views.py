from django.shortcuts import render , redirect , get_object_or_404
from .models import Appointment
from users.models import Doctor
from django.contrib.auth.decorators import login_required

from rolepermissions.decorators import has_role_decorator


@has_role_decorator('doctor')
@login_required(login_url='logIn')
def confirm_appointment(request , pk):
    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(Appointment, pk=pk , doctor=doctor)
    appointment.status = 'confirmed'
    appointment.save()
    return redirect("doctor_appointment")

@has_role_decorator('doctor')
@login_required(login_url='logIn')
def cancell_appointment(request, pk):
    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(Appointment, pk=pk, doctor=doctor)
    appointment.status = 'cancelled'
    appointment.save()
    return redirect("doctor_appointment")



@has_role_decorator('doctor')
@login_required(login_url='logIn')
def reschedule_appointment(request, pk):
    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(Appointment, pk=pk, doctor=doctor)
    appointment.status = 'pending'
    appointment.save()
    return redirect("doctor_appointment")

@has_role_decorator('doctor')
@login_required(login_url='logIn')
def undo_appointment(request, pk):
    doctor = Doctor.objects.get(user=request.user)
    appointment = get_object_or_404(Appointment, pk=pk, doctor=doctor)
    appointment.status = None
    appointment.save()

    return redirect("doctor_appointment")


@has_role_decorator('doctor')
@login_required(login_url='logIn')
def delete_appointment(request, pk):
    doctor = Doctor.objects.get(user=request.user)

    appointment = get_object_or_404(Appointment, pk=pk , doctor=doctor)
    appointment.delete()
    return redirect('doctor_appointment')

