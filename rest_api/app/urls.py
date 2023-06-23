from django.contrib import admin
from django.urls import path, include
from .views import *
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("data", views.Bookviewset, basename="Book")

urlpatterns = [
    # path("add/",views.booklist.as_view()),
    # path("delete/<int:id>/",views.booksdis.as_view()),
    path("", include(router.urls))
    ]
