
from django.contrib import admin
from django.urls import path , include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('appointments/', include("appointments.urls")),
    path("", views.home , name='home'),
]
