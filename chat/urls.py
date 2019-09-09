from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "chat"
urlpatterns = [
    path('chat/', views.index, name="index"),
    path('accounts/login/', LoginView.as_view(template_name='chat/login.html'), name="login"),
    path('chat/<str:room_name>/', views.room, name='room'),
]