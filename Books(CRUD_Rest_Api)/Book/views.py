from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def Booklist(request):
    bookobj = BooksModel.objects.all()
    serializer = BookSerializer(bookobj, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def post_book(request):
    bookobj = BooksModel.objects.all()
    serializer = BookSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def update_book(request,id):
    bookobj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance=bookobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_book(request,id):
    bookobj = BooksModel.objects.get(id=id)
    bookobj.delete()
    return Response("Book is deleted successfully")