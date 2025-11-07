from django.shortcuts import render
from .models import Patient

def patientList(request):
  patients = Patient.objects.all()
  