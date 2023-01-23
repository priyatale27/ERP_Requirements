from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics
from .serializers import *
from django.core import serializers as core_serializers
from django.db.models import Q


class RegisterAPIView(APIView):
    model = Login
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        role = data.get('role')
        hash_pass = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
        qs = Login.objects.filter(Q(id__iexact=id) | Q(email__iexact=email))
        if qs.count() == 0:
            user = Login.objects.create(email=email, password=hash_pass, name=name, role=role)
            user.save()            
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Thank you for Registering with us.You can sign in now'
            }
        else:
            response = {
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': 'this User id  or Email already taken, please choose another one'
            }

        return Response(response)


class LoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        role = Login.objects.filter(email=email).values('role')
        user_role = role[0]['role']
        user = Login.objects.get(email=email)
        hash_data = user.verify_password(password)
        if user_role == 'super_admin':
            if hash_data==True:
                request.session['email'] = user.id
                response = {
                    'status': status.HTTP_200_OK,
                    'email':user.email,
                    'id':user.id,
                    'message': 'Successfully Logged In'
                }
            else:
                response = {
                    'status': 'error',
                    'message': 'please check your user id or password'
                }
        elif user_role == 'main_admin':
            if hash_data==True:
                request.session['email'] = user.id
                response = {
                    'status': status.HTTP_200_OK,
                    'email':user.email,
                    'id':user.id,
                    'message': 'Successfully Logged In'
                }
            else:
                response = {
                    'status': 'error',
                    'message': 'please check your user id or password'
                }
        
        elif user_role == 'admin':
            if hash_data==True:
                request.session['email'] = user.id
                response = {
                    'status': status.HTTP_200_OK,
                    'email':user.email,
                    'id':user.id,
                    'message': 'Successfully Logged In'
                }
            else:
                response = {
                    'status': 'error',
                    'message': 'please check your user id or password'
                }        
        elif user_role == 'sub_admin':
            if hash_data==True:
                request.session['email'] = user.id
                response = {
                    'status': status.HTTP_200_OK,
                    'email':user.email,
                    'id':user.id,
                    'message': 'Successfully Logged In'
                }
            else:
                response = {
                    'status': 'error',
                    'message': 'please check your user id or password'
                }
        elif user_role == 'group_admin':
            if hash_data==True:
                request.session['email'] = user.id
                response = {
                    'status': status.HTTP_200_OK,
                    'email':user.email,
                    'id':user.id,
                    'message': 'Successfully Logged In'
                }
            else:
                response = {
                    'status': 'error',
                    'message': 'please check your user id or password'
                }
        else:
            response = {
                'status':"Error",
                'message':"Not Valid User"
            }

        return Response(response)
        

class UserDetailAPIView(APIView):

    def post(self, request):
        user_id = request.session['id']
        if user_id != request.session['id']:
            return redirect('This is not valid user_id')
        else:
            current_user = Login.objects.get(id=id)
