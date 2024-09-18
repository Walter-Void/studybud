from django.shortcuts import render, redirect
from django.contrib import messages #An import to help use show meassages
from django.contrib.auth.decorators import login_required #Import helps me restrict the user from doing things
from django.db.models import Q #Imports a way for me to use or and and on q 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout #import authenticate to work on login method 
from django.http import HttpResponse # imports to HttpsResponse to work
from .models import Room, Topic #Imports Room from the models.py
from .forms import RoomForm #imports Room form to this views


# Create your views here.

#List for rooms
#rooms = [
#    {'id': 1, 'name' : 'Lets learn python!'}, #Pretty much discord rooms
#    {'id': 2, 'name' : 'Design with me'},
#    {'id': 3, 'name' : 'Frontend developers'},
#]

#Function for logging in
def loginPage(request):
    if request.user.is_authenticated:
     return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # for other videos
        try:
            user = User.objects.get(username = username)
        except: 
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username = username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'User or Password does not exist')

    context = {}
    return render(request, 'base/login_register.html', context)

#Function/method to logout
def logoutUser(request):
    logout(request)
    return redirect('home')

#Function that shows user Home Page instead of the default page
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        ) #overrides the other room list 
    
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count' : room_count}
    return render(request, 'base/home.html', context) #Goes into template folder to go to the home html

#Function that show/sends you to a room
def room(request, pk):
    room = Room.objects.get(id =pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context) #Goes into template folder to go to the room html

@login_required(login_url = '/login') #only allows user to make a room
#Function that creates the room display on the Project
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context) 

@login_required(login_url = '/login') #only allows user to make a room
#Functions for updating the room
def updateRoom(request, pk):
    room = Room.objects.get(id =pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == "POST":
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url = '/login') #only allows user to make a room
#Function to delete room
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

