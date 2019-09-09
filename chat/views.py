from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers


def index(request):
    return render(request, "chat/index.html")

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