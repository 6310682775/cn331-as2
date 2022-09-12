from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
@login_required(login_url="/login")
def home(request):

    return render(request, 'main/home.html')

def registerSub(request):

    return render(request, 'main/registerSub.html')


