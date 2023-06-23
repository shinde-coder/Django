from django.urls import path
from . import views
urlpatterns = [
    path("", views.data_form, name="data_form"),
    path("data_read", views.data_read, name ="data_read"),
    path("delete/<int:id>", views.delete), 
    path("data_edit/<int:id>",views.data_edit),

    path('generate_invoice/<int:id>/', views.generate_invoice, name='generate_invoice'),

]
