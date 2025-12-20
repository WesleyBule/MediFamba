
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User , AbstractUser
from django.core.validators import RegexValidator

from datetime import date

moz_phone_validator = RegexValidator(
    regex=r'^\+258(8[234567])\d{7}$',
    message="Invalid Phone Number!"
)


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    birthDate = models.DateField(default="2000-01-01")
    speciality = models.CharField(max_length=120)
    residence = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(validators=[moz_phone_validator],max_length=14, unique=True, default="+258")
    profile = models.ImageField(upload_to="profiles/",blank=True, null=True , default='static/profile.png')

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    residence = models.CharField(max_length=50, default="")
    phoneNumber = models.CharField(validators=[moz_phone_validator],max_length=14, unique=True, default="+258 ")
    gender = models.CharField(max_length=8, choices=[('male',"Male"),('female','Female')], default="")
    birthDate = models.DateField()
    profile = models.ImageField(upload_to="profiles/",blank=True, null=True, default='static/profile.png')

    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.birthDate.year
            - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day) )
        )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"