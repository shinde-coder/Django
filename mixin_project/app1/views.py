from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     def get(self, request):
#         return self.list(request)
    
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     def post(self, request):
#         return self.create(request)

# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     def get(self, request, **kwargs):
#         return self.retrieve(request, **kwargs)
    
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializers
#     def put(self, request, **kwargs):
#         return self.update(request, **kwargs)

# class StudentDelete(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializers
#     def delete(self, request, **kwargs):
#         return self.destroy(request, **kwargs)
    
# # >>>>>>>>>>> Short Form of above classes <<<<<<<<<<<<<<<<<<<<<<<<
# class StudentListRetrieve(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
    
# class StudentRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, **kwargs):
#         return self.retrieve(request, **kwargs)
#     def put(self, request, **kwargs):
#         return self.update(request, **kwargs)
#     def delete(self, request, **kwargs):
#         return self.destroy(request, **kwargs)

# #>>>>>>>>>> Concrete Generic Views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class L_api(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class C_api(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class R_api(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class U_api(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class D_api(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
# #--------------------------------------------------------------------------------------
# class LC_api(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class RU_api(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class RD_api(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class RUD_api(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]