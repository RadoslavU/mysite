from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Здравей, Радо! Това е първата ти страница 🚀</h1>")
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')