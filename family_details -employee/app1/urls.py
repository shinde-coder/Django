from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('employes_list/', views.employes_list, name ="employes_list"),
    
    path("data_create", views.data_form, name="data_create"),
    path("data_read", views.data_read, name ="data_read"),
    path("delete/<int:id>", views.delete), 
    path("data_edit/<int:id>",views.data_edit),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]