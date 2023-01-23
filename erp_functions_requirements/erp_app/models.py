from django.db import models
from passlib.hash import pbkdf2_sha256
# Create your models here.

class Login(models.Model):
    ROLES_CHOICES = [
        ('super_admin','super_admin'),
        ('main_admin','main_admin'),
        ('admin','admin'),
        ('sub_admin','sub_admin'),
        ('group_admin','group_admin'),
        ('under_group_admin','under_group_admin'),
    ]
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=50, choices=ROLES_CHOICES, default='super_admin')        
    def verify_password(self,password):
        return pbkdf2_sha256.verify(password,self.password)


class Resident(models.Model):
    continent = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    taluka = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)