from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from django.db import models


class Employee(models.Model):
    eid = models.IntegerField(validators=[MinValueValidator(1)], unique=True)
    ename = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    eemail = models.EmailField(validators=[RegexValidator(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')])
    econtact = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    
    def __str__(self): 
        return "%s " %(self.ename)

    class Meta:
        db_table = "employee"
