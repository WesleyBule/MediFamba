from django.contrib import admin
from .models import Doctor , Patient , Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name','email','role']

    def get_queryset(self , request):
        qs = super().get_queryset(request)
        return qs.filter(role='patient')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user','speciality']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','user','birthDate','phoneNumber','gender']