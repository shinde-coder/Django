from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# Create your views here.
from .forms import TODOForm, CustomUserCreationForm
from .models import TODO
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )

def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'signup.html', context=context)
    else:
        form = CustomUserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)



@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})

@login_required(login_url='login')
def edit_todo(request, id):
    todo = get_object_or_404(TODO, id=id)
    if request.method == "POST":
        form = TODOForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TODOForm(instance=todo)
    return render(request, "edit_todo.html", {"form": form})

def delete_todo(request , id ):
    TODO.objects.get(pk = id).delete()
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login')