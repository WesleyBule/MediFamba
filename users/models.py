from django.db import models
from django.contrib.auth.models import User



class Doctor(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Dr. ")
    birthDate = models.DateField(default="1900-01-01")
    speciality = models.CharField(max_length=120)
    available_days = models.TextField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    residence = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(max_length=14, unique=True, default="+258 ")
    gender = models.CharField(max_length=8, choices=[('m',"Male"),('f','Female')], default="")
    birthDate = models.DateField()


    def __str__(self):
        return self.name