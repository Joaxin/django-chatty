from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers

@login_required
def index(request):
    return render(request, "chat/index.html")

def login(request):
    return render(request, "chat/login.html")

@login_required
def room(request, room_name):
    if request.user:
        print(request.user.username)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': serializers.serialize('json', [request.user,]),
        })
    else:
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': "visitor"
        })