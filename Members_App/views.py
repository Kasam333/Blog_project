from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
    return render(request, "index.html")

# Login view
def user_login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login_register.html", {"error": "Invalid credentials"})
        login(request, user)
        return redirect("home")  # Redirect to home view from Blog_App
    return render(request, "login_register.html")

def user_register(request):
    if request.method != 'POST':
        return render(request, "login_register.html")
    
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    if User.objects.filter(username = email).exists():
        messages.error(request, "Email is already registered.")
        return redirect("Register")
    
    user = User.objects.create_user(
        first_name = name,
        username= email,
        password=password
    )
    user.save()
    login(request, user)
    return redirect("home")

def user_logout(request):
    return redirect('Login')