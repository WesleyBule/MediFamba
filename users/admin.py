from django.contrib import admin
from .models import Doctor , Patient
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','is_staff','is_active','last_login']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user','name','speciality']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user','firstname','lastname','birthDate','phoneNumber','gender']