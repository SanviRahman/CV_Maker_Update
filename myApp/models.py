from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import User



class CustomUser(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name= models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)
   

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


class FormMaker(models.Model):
    image= models.ImageField(upload_to='images/', blank=True, null=True)
    mobile= models.CharField(max_length=15, blank=True, null=True)
    objective= models.TextField(max_length=1000, blank=True, null=True)
    skills= models.TextField(max_length=1000, blank=True, null=True)
    tools= models.TextField(max_length=1000, blank=True, null=True)
    projects= models.TextField(max_length=1000, blank=True, null=True)
    education= models.TextField(max_length=1000, blank=True, null=True)
    customuser= models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    

 
   