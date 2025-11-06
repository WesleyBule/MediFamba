from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=20,
        choices=[
        ('doctor','Doctor'),
        ('patient','Patient')])
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(Users , on_delete=models.CASCADE , limit_choices_to={'role':'doctor'})
    speciality = models.CharField(max_length=120)
    available_days = models.TextField()


class Patient(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE , limit_choices_to={'role':'patient '})
    age = models.IntegerField()
