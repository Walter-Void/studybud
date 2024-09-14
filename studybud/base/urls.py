from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), #Path to home 
    path('room/<str:pk>/', views.room, name = "room"), #Path to room
]