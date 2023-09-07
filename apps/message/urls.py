from django.urls import path
from . import views


urlpatterns = [
    path('send_message/', views.TelegramMessageListView.as_view()),
    
]