from django.urls import path
from .views import user_register


urlpatterns =[
    path("sign",user_register, name="signIn")
]