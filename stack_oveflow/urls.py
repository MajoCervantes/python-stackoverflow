import imp
from django.urls import path
from stack_oveflow import views

urlpatterns = [
    path("questions/", views.questions_list),
    path("questions/<int:pk>", views.questions_info),
]