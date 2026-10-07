
from datetime import date, datetime
import os

from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from courses.forms import CourseForm, UploadForm
from .models import Course ,Category, UploadModel
from django.core.paginator import Paginator

# Create your views here.
#FORMS
#Get => url = querystring
#Post => url = body



def index(request):

    kurslar = Course.objects.filter(isActive=True)
    kategori_listesi = Category.objects.all()
    courses = Course.objects.filter(isActive=True).order_by('date')

    paginator = Paginator(kurslar, 3)  # Her sayfada 2 kurs gösterilecek
    page = request.GET.get('page',1)  # GET parametresinden sayfa numarasını al
    page_obj = paginator.page(page)

   

    return render(request, 'courses/index.html', {
        "categories": kategori_listesi,
        "courses": courses
    })

def search(request):
    print(request.GET)  # GET parametrelerini yazdır
    query = request.GET.get('q', '')  # GET parametresinden arama sorgusunu al

    if query:
        kurslar = Course.objects.filter(isActive=True, title__contains=query).order_by('date')

        kategori_listesi = Category.objects.all()
    else:
        return redirect("/kurs")  # Eğer arama sorgusu boşsa anasayfaya yönlendir


    return render(request, 'courses/search.html', {
        "categories": kategori_listesi,
        "courses": kurslar,
        "page_obj": kurslar,
        "search_query": query  # Arama sorgusunu template'e gönder
    })

def create_kurs(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()  # Formu kaydet
           print(form.instance)  # Kaydedilen Course nesnesini yazdır
           return render(request, 'courses/details.html', {'course': form.instance})  # Kurs detay sayfasına yönlendir
    else:
        form = CourseForm()
    
    return render(request, 'courses/create_course.html', {"form": form})


def kurslar(request):
    return HttpResponse("<h1>Kurslar sayfası</h1>")

def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course_list.html', {
        "courses": kurslar,
    })

def course_edit(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course,)
        course.delete()  # Eski kursu sil
        form.save()  # Formu kaydet
       
        return render(request, 'courses/details.html', {'course': form.instance})
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/update_course.html', {"form": form, "course": course})

def course_delete(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == "POST":
        course.delete()  # Kursu sil
        return redirect('course_list')  # Kurs listesi sayfasına yönlendir

    return render(request, 'courses/course_delete.html', {"course": course})

def upload(request):

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)  # Formu oluştur
        if form.is_valid():
            
            model = UploadModel(image=form.cleaned_data['image'])  # Modeli oluştur
            model.save()  
            # Modeli kaydet

            return render(request, 'courses/success.html', {"image": model.image})  # Dosya bilgilerini template'e gönder
    else:
        form = UploadForm()  # Formu oluştur
        return render(request, 'courses/upload.html', {"form": form})  # Formu template'e gönder
    
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

    return render(request, 'courses/list.html', {
        "categories": kategoriler,
        "courses": page_obj,
        "page_obj": page_obj,
        "secili_kategori": slug

    })


   

