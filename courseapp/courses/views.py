
from datetime import date, datetime

from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course ,Category
from django.core.paginator import Paginator

# Create your views here.
#FORMS
#Get => url = querystring
#Post => url = body



def index(request):

    kurslar = Course.objects.filter(isActive=True)
    kategori_listesi = Category.objects.all()

    paginator = Paginator(kurslar, 3)  # Her sayfada 2 kurs gösterilecek
    page = request.GET.get('page',1)  # GET parametresinden sayfa numarasını al
    page_obj = paginator.page(page)

   

    return render(request, 'courses/index.html', {
        "categories": kategori_listesi,
        "courses": page_obj
    })

def search(request):
    print(request.GET)  # GET parametrelerini yazdır
    query = request.GET.get('q', '')  # GET parametresinden arama sorgusunu al

    if query:
        kurslar = Course.objects.filter(isActive=True, title__contains=query).order_by('date')

        kategori_listesi = Category.objects.all()
    else:
        return redirect("/kurs")  # Eğer arama sorgusu boşsa anasayfaya yönlendir

    paginator = Paginator(kurslar, 3)  # Her sayfada 2 kurs gösterilecek
    page = request.GET.get('page', 1)  # GET parametresinden sayfa numarasını al
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        "categories": kategori_listesi,
        "courses": page_obj,
        "page_obj": page_obj,
        "search_query": query  # Arama sorgusunu template'e gönder
    })



def kurslar(request):
    return HttpResponse("<h1>Kurslar sayfası</h1>")

def detay(request, slug): 
    
    """try:
            
        course = Course.objects.get(pk=kurs_id)
        
    except:
        raise Http404("Kurs bulunamadı...")"""

    course = get_object_or_404(Course, slug=slug)

    contex = {
                "course": course 
            }
    return render(request, 'courses/details.html', contex)



def getCoursesByCategory(request, slug):

    kurslar = Course.objects.filter(categories__slug=slug, isActive= True).order_by('date')

    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 3)  # Her sayfada 2 kurs gösterilecek
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    print(page_obj.paginator.num_pages)
    print(page_obj.paginator.count)

    return render(request, 'courses/index.html', {
        "categories": kategoriler,
        "courses": page_obj,
        "page_obj": page_obj,
        "secili_kategori": slug

    })


   

