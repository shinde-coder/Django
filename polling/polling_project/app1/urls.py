from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index" ),
    path("detail/<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("data_form/", views.data_form, name="data_form"),
    path("delete/<int:id>", views.delete), 
    path("data_edit/<int:id>",views.data_edit)
]