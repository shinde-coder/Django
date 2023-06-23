from django.shortcuts import render
from .serializer import *
from .models import *
#from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# # Create your views here.

# class booklist(GenericAPIView, ListModelMixin,CreateModelMixin):
#     queryset = BooksModel.objects.all()
#     serializer_class= BookSerializer
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
# class booksdis(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset= BooksModel.objects.all()
#     serializer_class= BookSerializer
#     def get(self, request,**kwargs):
#         return self.retrieve(request, **kwargs)
#     def put(self, request,**kwargs):
#         return self.update(request, **kwargs)
#     def delete(self, request,**kwargs):
#         return self.destroy(request, **kwargs)
    
    

#model view set

class Bookviewset(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class=BookSerializer