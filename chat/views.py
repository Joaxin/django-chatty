from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import json

@login_required
def index(request):
    return render(request, "chat/index.html")

def login(request):
    return render(request, "registration/login.html")

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
