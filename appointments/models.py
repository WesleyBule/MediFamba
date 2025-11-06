from django.db import models
from users.models import Users

class Appointment(models.Model):
    patient = models.ForeignKey(Users,on_delete=models.CASCADE , 
        related_name='appointments' , limit_choices_to={'role':'patient'})
    doctor = models.ForeignKey(Users, on_delete=models.CASCADE,
        related_name='doctor_appointments', limit_choices_to={'role':'doctor'})
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Canceled')
    ])