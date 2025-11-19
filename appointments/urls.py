from django.urls import path

from . import views


urlpatterns = [
    path("confirm/<int:pk>", views.confirm_appointment, name='confirm_appointment'),
    path("cancell/<int:pk>", views.cancell_appointment, name='cancell_appointment'),
    #path("reschedule/<int:pk>", views.reschedule_appointment, name='reschedule_appointment'),
    path("delete/<int:pk>", views.delete_appointment, name='delete_appointment'),
    path("undo/<int:pk>", views.undo_appointment, name='undo_appointment')
]