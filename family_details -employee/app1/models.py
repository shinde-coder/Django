from django.db import models
from django.contrib.auth.models import User


class relation(models.Model):
    relation = models.CharField(max_length=50)
    def __str__(self):
            return self.relation

gender =(
     ("A","Select"),
     ("Male","Male"),
     ("Female","Female")
)

#family_details Model
from django.core.exceptions import ValidationError

class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gender, default="A")
    is_head = models.BooleanField(null=True, default=False)
    relation = models.ForeignKey(relation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def clean(self):
        if self.is_head:
            existing_heads = Employee.objects.filter(is_head=True)
            if existing_heads.exists():
                raise ValidationError('There can be only one head Member in the family.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
         return str(self.relation)



                                                                            
