from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from appointments.models import Appointment
from django.forms import ClearableFileInput

from .models import Patient , Doctor

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists")
        return email



class ScheduleAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'date'
        ]
        widgets = {
            'date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                    'style': 'max-width: 300px'
                },
                format='%Y-%m-%dT%H:%M'
            )
        }



class PatientSettingsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['profile']
        widgets = {
        'profile': ClearableFileInput(attrs={
            'class': 'clearablefileinput profile-upload-input'
            })
        }



class DoctorSettingsForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['profile']
        widgets = {
        'profile': ClearableFileInput(attrs={
            'class': 'clearablefileinput profile-upload-input'
            })
        }
