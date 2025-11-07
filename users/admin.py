from django.contrib import admin
from .models import Doctor , Patient
from django.contrib.auth.models import User


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','speciality']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','birthDate','phoneNumber','gender']