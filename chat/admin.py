from django.contrib import admin

# Register your models here.
from .models import Message

from .models import Contact, Message

admin.site.register(Contact)
admin.site.register(Message)