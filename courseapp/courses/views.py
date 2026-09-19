
from datetime import date, datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

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

    kurslar = [course for course in db["courses"] if course["isActive"]]
    kategori_listesi = db["categories"]
    

    return render(request, 'courses/index.html', {
        "categories": kategori_listesi,
        "courses": kurslar
    })

def kurslar(request):
    return HttpResponse("<h1>Kurslar sayfası</h1>")

def detay(request, kurs_adi): 
    return HttpResponse(f"{kurs_adi} kurs detayları...")   

def getCoursesByCategory(request, category_name):

    try: 
        text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name, 
            "category_text": text

        }
            )
    except :
        return HttpResponseNotFound("Kategori bulunamadı...")

def getCoursesByCategoryId(request, category_id):
    #return HttpResponseRedirect(f'/kurs/kategori/programlama')

    category_list = list(data.keys())

    if category_id < 1 or category_id > len(category_list):
        return HttpResponseNotFound("Kategori bulunamadı...")
    
    category = category_list[category_id - 1]

    redirect_url = reverse('getCoursesByCategory', args=[category])

    return redirect(redirect_url)
