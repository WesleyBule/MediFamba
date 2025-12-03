from django.urls import path

from . import views


urlpatterns = [
    path("confirm/<uuid:id>", views.confirm_appointment, name='confirm_appointment'),
    path("cancell/<uuid:id>", views.cancell_appointment, name='cancell_appointment'),
    #path("reschedule/<int:pk>", views.reschedule_appointment, name='reschedule_appointment'),
    path("delete/<uuid:id>", views.delete_appointment, name='delete_appointment'),
    path("undo/<uuid:id>", views.undo_appointment, name='undo_appointment')
]