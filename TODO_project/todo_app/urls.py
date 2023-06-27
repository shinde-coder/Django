
from django.contrib import admin
from django.urls import path
from .views import home , login , signup , add_todo , signout , delete_todo,  edit_todo


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path("edit_todo/<int:id>", edit_todo, name= "edit_todo"),
   path('delete-todo/<int:id>' , delete_todo, name= "delete_todo"), 
   path('logout/' , signout ), 
]