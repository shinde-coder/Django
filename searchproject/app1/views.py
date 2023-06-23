from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    if "q" in request.GET:
        q = request.GET['q']
        multipleQ = Q(Q(first_name__icontains=q)|Q(last_name__icontains=q)|Q(age__icontains=q))
        obj = Data.objects.filter(multipleQ)
    else:
        obj = Data.objects.all()
    return render(request,"dashboard/index.html",{"obj":obj})