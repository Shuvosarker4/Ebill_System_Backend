from django.db import models
from users.models import User
from uuid import uuid4

# Create your models here.
class Customer(models.Model):
    CONNECTION_CHOICES = [
        ('Fiber', 'Fiber'),
        ('DSL', 'DSL'),
        ('Broadband', 'Broadband'),
    ]

    WIFI_PLAN_CHOICES = [
        ('Basic-5', 'Basic - 5 Mbps'),
        ('Standard-10', 'Standard - 10 Mbps'),
        ('Premium-100', 'Premium - 100 Mbps'),
        ('Ultra-200', 'Ultra - 200 Mbps'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True, db_index=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    connection_type = models.CharField(max_length=50, choices=CONNECTION_CHOICES)
    connection_date = models.DateTimeField(auto_now_add=True)
    wifi_plan = models.CharField(max_length=50, choices=WIFI_PLAN_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.connection_type} - {self.wifi_plan}"
