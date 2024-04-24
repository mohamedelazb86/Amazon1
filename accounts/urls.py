from django.urls import path
from .views import sigup,activate_code

urlpatterns = [
    path('signup',sigup),
    path('<str:username>/activate',activate_code),
]
