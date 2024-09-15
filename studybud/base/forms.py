from django.forms import ModelForm
from .models import Room

#creating a form for the rooms 
class RoomForm(ModelForm):
    class Meta:
        model = Room 
        fields = '__all__'