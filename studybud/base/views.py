from django.shortcuts import render
from django.http import HttpResponse # imports to HttpsResponse to work

# Create your views here.

#Function that shows user Home Page instead of the default page
def home(request):
    return render(request, 'home.html') #Goes into template folder to go to the home html

#Function that show/sends you to a room
def room(request):
    return render(request, 'room.html') #Goes into template folder to go to the room html