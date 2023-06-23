from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    emp = Employee.objects.all()
    return render(request, 'index.html',{"emp":emp})


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html',context)

    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            emps = Employee.objects.all()
            context = {
                'emps': emps
            }
            return render(request, 'view_all_emp.html',context)
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
    
        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
    
def update_emp(request, emp_id=id):
    if request.method == 'POST':
        try:
            employee = Employee.objects.get(id=emp_id)
            employee.first_name = request.POST['first_name']
            employee.last_name = request.POST['last_name']
            employee.salary = int(request.POST['salary'])
            employee.bonus = int(request.POST['bonus'])
            employee.phone = int(request.POST['phone'])
            employee.dept_id = int(request.POST['dept'])
            employee.role_id = int(request.POST['role'])
            employee.save()
            emps = Employee.objects.all()
            context = {
                'emps': emps
            }
            return render(request, 'view_all_emp.html',context)
        except Employee.DoesNotExist:
            return HttpResponse('Invalid Employee ID')
    elif request.method == 'GET':
        try:
            employee = Employee.objects.get(id=emp_id)
            departments = Department.objects.all()
            roles = Role.objects.all()
            context = {
                'employee': employee,
                'departments': departments,
                'roles': roles
            }
            return render(request, 'update_emp.html', context)
        except Employee.DoesNotExist:
            return HttpResponse('Invalid Employee ID')
    else:
        return HttpResponse('An exception occurred')
