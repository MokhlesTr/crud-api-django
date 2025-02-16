from django.urls import path
from . import views
from .views import api_members

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path("addrec", views.addrec, name="addrec"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path('api/members/', api_members, name='api_members'),  # For GET all, POST new member
    
    # For member actions by ID (GET, PUT, DELETE)
    path('api/members/<int:id>/', api_members, name='api_member_detail'),  # Handle GET, PUT, DELETE for specific member
]
