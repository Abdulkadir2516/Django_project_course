
from datetime import date, datetime

from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course ,Category
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    kurslar = Course.objects.filter(isActive=True)
    kategori_listesi = Category.objects.all()

    paginator = Paginator(kurslar, 2)  # Her sayfada 2 kurs gösterilecek
    page = request.GET.get('page')  # GET parametresinden sayfa numarasını al
    course_page = paginator.get_page(page)

    print(paginator.num_pages)
    print(course_page.number)
    print(paginator.count)

    return render(request, 'courses/index.html', {
        "categories": kategori_listesi,
        "courses": course_page
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

    paginator = Paginator(kurslar, 2)  # Her sayfada 2 kurs gösterilecek
    page = 1 
    course_page = paginator.get_page(page)

    return render(request, 'courses/index.html', {
        "categories": kategoriler,
        "courses": course_page,
        "secili_kategori": slug

    })


   

