from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('add/', views.add,name="add"),
    path("addrec",views.addrec,name="addrec"),
    path("delete/<int:id>/",views.delete,name="delete"),


]
