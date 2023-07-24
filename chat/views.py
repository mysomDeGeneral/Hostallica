from django.shortcuts import render
from backend.models import Student, Hall, Room



def index(request):
    return render(request, 'chathome.html')


def room(request, room):
    return render(request, 'chatroom.html')