from django.db import models

class Position(models.Model):
    position = models.CharField(max_length=20)
    def __str__(self):
            return self.position

class Report_to(models.Model):
    report_to = models.CharField(max_length=20, default=True, null=True)
    def __str__(self):
            return self.report_to

class Employee(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_ceo = models.BooleanField(null=True)
    position = models.ForeignKey(Position , on_delete=models.CASCADE)
    report_to = models.ForeignKey(Report_to , on_delete=models.CASCADE, null=True, blank=True)
    



