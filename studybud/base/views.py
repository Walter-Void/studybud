from django.shortcuts import render, redirect
from django.db.models import Q #Imports a way for me to use or and and on q 
from django.contrib.auth.models import User
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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # for other videos
        #try:
        #    user = User.objects.get(username = username)
        #except: 

    context = {}
    return render(request, 'base/login_register.html', context)

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

#Functions for updating the room
def updateRoom(request, pk):
    room = Room.objects.get(id =pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

#Function to delete room
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

