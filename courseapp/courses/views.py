from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Kurslar anasayfası")

def kurslar(request):
    return HttpResponse("Kurslar listeleniyor...")

def detay(request): 
    return HttpResponse("Kurs detayları...")   

def programlama(request):
    return HttpResponse("Programlama kursları listeleniyor...")

def mobil_uygulamalar(request):
    return HttpResponse("Mobil uygulamalar kursları listeleniyor...")