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
        

class LoginUnderGroupAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        role = Login.objects.filter(email=email).values('role')
        user_role = role[0]['role']
        user = Login.objects.get(email=email)
        hash_data = user.verify_password(password)
        if user_role == 'under_group_admin':
            if username == 'username':
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
            elif otp == 'otp':
                try:
                    params=request.data
                    try:
                        mobile_number=params.pop("mobile_number")
                    except Exception:
                        mobile_number=None
                    if not mobile_number:
                        return Response({"status":False,"message":"Please Enter your phone number !!!!!"},status=status.HTTP_400_BAD_REQUEST)
                    if not  Login.objects.filter(mobile_number=mobile_number):
                        return Response({"status":False,"message":"This mobile number is not yet registered !!!!!"},status=status.HTTP_400_BAD_REQUEST)
                    otp=generate_otp()
                    send_otp(mobile_number,otp)
                    return Response({"status":True,"message":"We have sent an otp on your mobile number !!!!!!"},status=status.HTTP_200_OK)
                except Exception:
                    print("Exception is occured")
                    return Response({"status":False,"message":"Something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(response)


class UserDetailAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        continent = data.get('continent')
        country = data.get('country')
        state = data.get('state')
        district = data.get('district')
        taluka = data.get('taluka')
        village = data.get('village')
        response = {
            'continent':continent,
            'country':country,
            'state':state,
            'district':district,
            'taluka':taluka,
            'village':village,
        }

        return Response(response)