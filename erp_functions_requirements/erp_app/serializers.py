from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    password = serializers.CharField(
        write_only=True, required=True)

    class Meta:
        model = Login
        fields = ('email', 'password', 'name', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Login.objects.create(
        email=validated_data['email'],
        name=validated_data['name'],
        role = validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#class UserLoginSerializer(serializers.ModelSerializer):
