
from django.contrib import admin
from django.urls import path , include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path("appointments/", include("appointments.urls")),

    
    path("", views.root_redirect , name='root_redirect'),

    path("user/", views.home_user, name="home_user"),
    path("info/",views.information, name='info'),

    path("doctors/",views.home_doctor, name="home_doctor"),
    path("doctors/appointments",views.appointmentList, name="doctor_appointment"),
    path("doctors/patients",views.patientList, name="doctor_patients"),

    path("patients/", views.home_patients, name="home_patient"),
    path("patients/agenda", views.agendaList,name='patients_agenda'),
    path("patients/doctors", views.doctorList, name="patient_doctors"),
    path("patients/book",views.bookAppointment, name="patient_book_appointment"),





]
