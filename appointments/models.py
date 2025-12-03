import uuid
from django.db import models
from users.models import Patient , Doctor

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE , 
        related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
        related_name='doctor_appointments')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, null = True , blank = True , choices=[
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled')])
