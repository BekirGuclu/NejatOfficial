from django.shortcuts import render
from .forms import ContactForm

def sendMessage(request):
    form = ContactForm()
    return render(request, "contact.html", {"form":form},)
# Create your views here.
