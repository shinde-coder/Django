from django.urls import path
from org_app import views

urlpatterns = [
    #create
    path("data_create", views.data_form, name="data_create"),
    #read
    path("data_read", views.data_read, name ="data_read"),
    path("delete/<int:id>", views.delete), 
    path("report_to", views.report_to),
    
]