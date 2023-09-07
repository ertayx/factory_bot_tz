from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('telegram_token/', views.TokenUpdateView.as_view()),

]