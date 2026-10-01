from django.shortcuts import render
from django.http import HttpResponse
from .forms import OnlineAccess


def online(request):
    form = OnlineAccess()
    
    if request.method == "POST":
        form = OnlineAccess(request.POST)
        if form.is_valid():
            
            return HttpResponse("You are signed up for online access!")
    return render(request, "profile_creation.html", {"form": form})