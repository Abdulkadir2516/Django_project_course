from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Anasayfa")

def iletisim(request):
    return HttpResponse("İletişim sayfası")

def hakkimizda(request):
    return HttpResponse("Hakkımızda sayfası")