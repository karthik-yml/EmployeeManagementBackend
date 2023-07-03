from django.contrib import admin
from django.urls import path, include
from . views import EmployeeRegisterView, LoginView

urlpatterns = [
    path('register/', EmployeeRegisterView.as_view()),
    path('login/', LoginView.as_view())
]