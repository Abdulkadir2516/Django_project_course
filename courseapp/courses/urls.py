from django.urls import path
from . import views

# http://127.0.0.1:8000/client            => anasayfa
# http://127.0.0.1:8000/client/home        => anasayfa
# http://127.0.0.1:8000/client/kurslar     => anasayfa



urlpatterns = [   
    path('', views.index, name='index'),  
    path('search', views.search, name='search'),
    path('create-kurs', views.create_kurs, name='create_course'),

    path('<slug:slug>', views.detay, name='course_details'),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name='getCoursesByCategory'),
    

]