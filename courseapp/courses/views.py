
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama": "Programlama kategorisine göre kurslar listeleniyor...",
    "mobil-uygulamalar": "Mobil uygulamalar kategorisine göre kurslar listeleniyor...",
    "web-gelistirme": "Web geliştirme kategorisine göre kurslar listeleniyor...",
    
}


# Create your views here.
def index(request):
    categories_list = list(data.keys())

    


    return render(request, 'courses/index.html', {
        "categories": categories_list
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
