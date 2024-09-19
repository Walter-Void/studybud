from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = "login"), #Path to login
    path('logout/', views.logoutUser, name = "logout"), #Path to logou
    path('register/', views.registerPage, name = "register"), #Path to register a user

    path('', views.home, name = "home"), #Path to home 
    path('room/<str:pk>/', views.room, name = "room"), #Path to room
    path('profile/<str:pk>/', views.userProfile, name = "user-profile"), #Path to user profile 

    path('create-room/', views.createRoom, name = "create-room"),#Path for room_form
    path('update-room/<str:pk>/', views.updateRoom, name = "update-room"), #Path for forms
    path('delete-room/<str:pk>/', views.deleteRoom, name = "delete-room"), #Path to delete rooms
    path('delete-message/<str:pk>/', views.deleteMessage, name = "delete-message"), #Path to delete message
]