from django.db import models

# Create your models here. 
class Service(models.Model):
    service_icon = models.CharField(max_length=60,default='')
    service_title = models.CharField(max_length=50,default='')
    service_des = models.TextField(max_length=60,default='')

def __str__(self):
    self.service_icon