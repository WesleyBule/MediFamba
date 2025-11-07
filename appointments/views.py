from django.shortcuts import render
from .models import Appointment


def appointmentList(request):
  appointments = Appointment.objects.all()
  context = {
    "appointments":appointments,
  }
  return render(request,"appointments/appointments.html",context)
