from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employeeform
# Create your views here.

def data_form(request):
    if request.method=="POST":
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("data_read")
    else:
        form = Employeeform()
        return render(request, "data_form.html", {"form":form})


def data_read(request):
    context = {"data_read": Employee.objects.all}
    return render(request, "data_read.html",context)

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/data_read")

def report_to(request, id):
    employee = Employee.objects.get(id=id)
    if employee.position == "team_lead":
        employee.report_to = employee.name
        b = employee.report_to
        return render(request, "data_read.html", {"b":b})














































































def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = Employeeform(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/data_read")  
    return render(request, 'edit.html', {'employee': employee})  