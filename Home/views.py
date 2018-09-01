from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view(request): #view olması için en az 1 tane argüman almalı
    return render(request, 'home.html', {}) #ilk argüman olmalı, ikincisi html çıktısı, {} => anahtar

# Create your views here.
