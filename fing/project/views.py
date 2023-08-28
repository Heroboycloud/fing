from django.shortcuts import render
from django.urls import reverse
from django.db.models import Max
from django.utils import timezone
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from .models import Category, Project

def index(request):
    obj = Project.objects.filter(active=True)
    return render(request, "projects/index.html", {
        "objects": obj
    })
    
def all(request):
    obj = Project.objects.all()
    return render(request, "projects/index.html", {
        "objects": obj
    })

def contact(request):
    return render (request,"projects/contact.html")
    
def subscribe(request):
    return render (request,"projects/landing.html")
    
    
def categories(request):
    if request.method == 'POST':
        category = request.POST["category"]
        new_category, created = Category.objects.get_or_create(
            name=category.lower())
        if created:
            new_category.save()
        else:
            messages.warning(request, "Category already Exists!")
        return HttpResponseRedirect(reverse("categories"))
    return render(request, "projects/categories.html", {
        'categories': Category.objects.all()
    })
    
def filter(request, name):
    category = Category.objects.get(name=name)
    obj = Project.objects.filter(category=category)
    return render(request, "projects/index.html", {
        "objects": obj
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "accounts/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "accounts/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "accounts/register.html")



  
  
def details(request, id):
    item = Project.objects.get(id=id)
    
    return render(request, "projects/detail.html", {
        'item': item,
        
        
    })
