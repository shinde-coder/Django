from django.contrib import admin

# Register your models here.

from .models import Employee,Position,Report_to

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Report_to)

