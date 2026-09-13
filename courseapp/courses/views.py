from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Anasayfa")

def kurslar(request):
    return HttpResponse("Kurslar listeleniyor...")