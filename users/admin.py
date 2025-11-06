from django.contrib import admin
from .models import Doctor , Patient , Users

admin.site.register(Users)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user','speciality',]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user','age']