from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    test = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_customers')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_customers')

    def __str__(self):
        return self.name