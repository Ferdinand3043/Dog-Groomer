from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import AboutUs


def home(request):
    return HttpResponse("Groomer Homepage")

def information(request):
    Details = AboutUs.objects.all()
    return render(request, 'about.html', {"Details": Details})


def contact(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
            return HttpResponse("Thank you for your message.")
        
    return render(request, "contact.html", {"form": form})