from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

# def home(request):
#     return HttpResponse('<h1>this is home</h1>')

def about(request):
    return HttpResponse('<h1>this is about</h1>')

def home(request):
    
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all
    return render(request=request, 
                  template_name = 'home.html', 
                  context={'searchTerm':searchTerm, 'movies':movies})

def signup(request):
    email = request.GET.get('email')
    return render(request=request, 
                  template_name = 'email.html', 
                  context={'email':email})
