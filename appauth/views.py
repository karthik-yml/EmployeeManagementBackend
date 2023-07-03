from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .authenticate import EmailBackend
# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . serializers import EmployeeRegistrationSerializer, LoginSerializer
from django.contrib.auth.hashers import check_password

class EmployeeRegisterView(GenericAPIView):
    serializer_class = EmployeeRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()

        response_data = {
            'message': 'Employee registered successfully',
            'employee_id': employee.employee_id,
            'email': employee.email,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer  
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = EmailBackend.authenticate(request, email, password)
        if user is not None:
            login(request, user)
            request.session['logged_in'] = True
            request.session['email'] = email
            return Response({"message": "You are logged in"}, status=status.HTTP_200_OK)
        else:
            error_message = "Invalid email or password."
            return Response({'error_message': error_message}, status=status.HTTP_401_UNAUTHORIZED)
