from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Employee
from .forms import Employeeform

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


from django.db import IntegrityError

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if(len(uname)==0 or len(email)==0 or len(pass1)==0 or len(pass2)==0):
            return HttpResponse("Please fill all the details!")
        if pass1!=pass2:
            return HttpResponse("Your password and confrim password are not Same!!")
        else:
            try:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                return HttpResponse("A user with that username already exists. Please choose a different username.")

    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('data_read')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def employes_list(request):
    employees = Employee.objects.all()
    return render(request, 'registration_list.html', {'employees': employees})


@login_required
def employes_list(request):
    users = User.objects.all()
    return render(request, 'registration_list.html', {'users': users})

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

    # Retrieve the common records for the selected usernames
    common_records = Employee.objects.filter(user=request.user)
    context = {
        "data_read": common_records,
    }
    return render(request, "data_read.html", context)


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/data_read")

def data_edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("data_read")
    else:
        form = Employeeform(instance=employee)
    return render(request, "data_form.html", {"form":form})