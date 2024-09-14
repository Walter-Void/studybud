from django.shortcuts import render
from django.http import HttpResponse # imports to HttpsResponse to work

# Create your views here.

#List for rooms
rooms = [
    {'id': 1, 'name' : 'Lets learn python!'}, #Pretty much discord rooms
    {'id': 2, 'name' : 'Design with me'},
    {'id': 3, 'name' : 'Frontend developers'},
]
#Function that shows user Home Page instead of the default page
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context) #Goes into template folder to go to the home html

#Function that show/sends you to a room
def room(request, pk):
    room = None
    for i in rooms: #for loop 
        if i['id'] == int(pk):
            room = i 
    context = {'room' : room}
    return render(request, 'base/room.html', context) #Goes into template folder to go to the room html