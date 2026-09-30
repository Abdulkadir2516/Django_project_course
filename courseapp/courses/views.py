
from datetime import date, datetime

from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course ,Category

data = {
    "programlama": "Programlama kategorisine göre kurslar listeleniyor...",
    "mobil-uygulamalar": "Mobil uygulamalar kategorisine göre kurslar listeleniyor...",
    "web-gelistirme": "Web geliştirme kategorisine göre kurslar listeleniyor...",
    
}

db = {
    "courses": [
        {
            "title": "Python Programlama",
            "description": "Python programlama dili ile ilgili kurslar listeleniyor...",
            "image": "python.jpeg",
            "slug": "python-programlama",
            "date": datetime.now(),
            "isActive": True,
            "isupdated": True
        },
        {
            "title": "Java Programlama",
            "description": "Java programlama dili ile ilgili kurslar listeleniyor...",
            "image": "java.jpg",
            "slug": "java-programlama",
            "date": date(2023, 1, 1),
            "isActive": False,            
            "isupdated": True

        },
        {
            "title": "C# Programlama",
            "description": "C# programlama dili ile ilgili kurslar listeleniyor...",
            "image": "c-sharp.jpeg",
            "slug": "csharp-programlama",
            "date": date(2023, 1, 1),
            "isActive": True,
            "isupdated": False

        },
        {
            "title": "JavaScript Programlama",
            "description": "JavaScript programlama dili ile ilgili kurslar listeleniyor...",
            "image": "javascript.jpg",
            "slug": "javascript-programlama",
            "date": date(2023, 1, 1),
            "isActive": False,
            "isupdated": False

        },
        {
            "title": "PHP Programlama",
            "description": "PHP programlama dili ile ilgili kurslar listeleniyor...",
            "image": "php.jpg",
            "slug": "php-programlama",
            "date": date(2023, 1, 1),
            "isActive": True,
            "isupdated": True
        }

    ],
    "categories": [
        {"id":1, "name": "Programlama", "slug": "programlama"},
        {"id":2, "name": "Mobil Uygulamalar", "slug": "mobil-uygulamalar"},
        {"id":3, "name": "Web Geliştirme", "slug": "web-gelistirme"}
    ]
}
# Create your views here.

def index(request):

    kurslar = Course.objects.filter(isActive=True)
    kategori_listesi = Category.objects.all()
    

    return render(request, 'courses/index.html', {
        "categories": kategori_listesi,
        "courses": kurslar
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

    kurslar = Course.objects.filter(category__slug=slug, isActive= True)

    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        "categories": kategoriler,
        "courses": kurslar,
        "secili_kategori": slug

    })


   

