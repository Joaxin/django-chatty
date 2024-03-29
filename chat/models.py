from django.db import models
from django.contrib.auth.models import User
import datetime

class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='contacts')
        
    contacts = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}({self.timestamp})"

    def get_last_messages(num):
        return reversed(Message.objects.order_by('-timestamp').all()[:num])
