from django.urls import path
from .views import appointmentList
urlpatterns =[
    path("", appointmentList, name="appointments")
]