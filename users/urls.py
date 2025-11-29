from django.urls import path
from . import views

urlpatterns =[
    path("sign/",views.user_register, name="signUp"),
    path("login/", views.user_login, name="logIn"),
    path("logout/", views.user_logout, name="logOut"),

]