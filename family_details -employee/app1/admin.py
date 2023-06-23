from django.contrib import admin

# Register your models here.

from .models import Employee,relation

admin.site.register(Employee)
admin.site.register(relation)   