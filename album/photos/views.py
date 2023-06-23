from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def gallery(request):
    cat = request.GET.get("cat")
    if cat == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = cat)

    obj = Category.objects.all()

    context = {
        "obj": obj,
        "photos": photos
    }

    return render(request, "gallery.html", context)


def add(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                discription=data['discription'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'add.html', context)

def photo(request, pk):
    obj = Photo.objects.get(id=pk)
    return render(request, "photo.html",{"obj": obj}) 