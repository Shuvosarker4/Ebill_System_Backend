from django.db import models
from customer.models import Customer
from uuid import uuid4


class Bill(models.Model):
    MONTH_CHOICES = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
    ]

    PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('card', 'Credit/Debit Card'),
    ('bank', 'Bank Transfer'),
    ('online', 'Online Payment'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bills')
    billing_month = models.CharField(max_length=2, choices=MONTH_CHOICES, default='01')
    billing_year = models.IntegerField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    payment_reference = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Bill for {self.customer} - {self.billing_month}/{self.billing_year}"
