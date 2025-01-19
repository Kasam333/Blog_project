from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Landing page (index.html)
    path("login/", views.user_login, name="Login"),  # Login page
    path("logout/", views.user_logout, name = "Logout"),
    path("register/", views.user_register, name="Register"),  # Registration page
    
]
