
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User , AbstractUser

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    birthDate = models.DateField(default="2000-01-01")
    speciality = models.CharField(max_length=120)
    residence = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(max_length=14, unique=True, default="+258 ")
    profile = models.ImageField(null=True, blank=True,  default='default.jpg')

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    residence = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(max_length=13, unique=True, default="+258 ")
    gender = models.CharField(max_length=8, choices=[('M',"Male"),('F','Female')], default="")
    birthDate = models.DateField()
    profile = models.ImageField(blank=True, null=True , default='default.jpg')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"