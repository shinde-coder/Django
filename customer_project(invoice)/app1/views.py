from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def data_form(request):
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("data_read")
    else:
        form = CustomerForm()
        return render(request, "data_form.html", {"form":form})


def data_read(request):
    context = {"data_read": Customer.objects.all}
    return render(request, "data_read.html",context)

def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/data_read")

def data_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("data_read")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "data_form.html", {"form":form})

def generate_invoice(request, id):
    customer = get_object_or_404(Customer, id=id)
    test_list = customer.test.split(',')
    context = {
        "customer": customer,
        "test_list": test_list,
    }
    return render(request, "invoice.html", context)