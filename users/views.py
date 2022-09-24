from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
        "users" : users.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    users.objects.create(first_name = request.POST['firstName'], last_name = request.POST['lastName'], email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')
