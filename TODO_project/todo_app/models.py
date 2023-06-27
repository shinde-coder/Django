from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=(("C","Completed"),("F","Pending")))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),))

    def __str__(self):
        return self.title


