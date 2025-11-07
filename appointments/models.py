from django.db import models
from users.models import Users , Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE , 
        related_name='appointments')
    doctor = models.ForeignKey(Users, on_delete=models.CASCADE,
        related_name='doctor_appointments', limit_choices_to={'role':'doctor'})
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Canceled')
    ])