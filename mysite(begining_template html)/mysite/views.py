from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
from service.models import Service

# def about_us(request):
#     return HttpResponse("Welcome to my site")
def home(request):
    return render(request, "index.html")
def about_us(request):
    if request.method == "GET":
        output=request.GET.get('output')
    return render(request, "about.html", {'output': output})
def contact_us(request):
    return render(request,"contact.html")


def userform(request):
    finalans=0
    fn=usersForm()
    data = {'form': fn}
    try:
        if request.method =="POST":
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalans = n1+n2
            data={
                'form': fn,
                'output':finalans
            }
            url = "/about/?output={}".format(finalans)

            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",{'output':finalans})
def prac(request):
    c=0
    try:
        if request.method =="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr = request.POST.get("opr")
            print(n1)
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            else:
                c=n1/n2
    except:
        c="invalid input"

    print(c)
    return render(request,"prac.html",{'c':c})
def even_odd(request):
    c=0
    if request.method == "POST":
        
        if request.POST.get("even_odd")=="":
            return render(request, "even_odd.html",{'error':True})
        
        n1= eval(request.POST.get("even_odd"))
        if n1%2==0:
            c= "even"
        else:
            c= "odd"
    return render(request, "even_odd.html",{'c':c})

def prac1(request):
    serviceData =Service.objects.all().order_by('service_icon')
    data = {
        'serviceData': serviceData
    }
    return render(request, "prac1.html",data)

