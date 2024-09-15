from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), #Path to home 
    path('room/<str:pk>/', views.room, name = "room"), #Path to room
    path('create-room/', views.createRoom, name = "create-room"),#Path for room_form
    path('update-room/<str:pk>/', views.updateRoom, name = "update-room"), #Path for forms
     path('delete-room/<str:pk>/', views.deleteRoom, name = "delete-room"), #Path to delete rooms
]