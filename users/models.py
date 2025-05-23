from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    ADMIN = 'Admin'
    CONSUMER = 'Consumer'
    STATUS_ROLES = [
        (ADMIN, 'Admin'),
        (CONSUMER, 'Consumer'),
    ]
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=200,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=10, choices=STATUS_ROLES,default=CONSUMER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
