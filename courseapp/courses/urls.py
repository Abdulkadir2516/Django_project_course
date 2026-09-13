from django.urls import path
from . import views

# http://127.0.0.1:8000/client            => anasayfa
# http://127.0.0.1:8000/client/home        => anasayfa
# http://127.0.0.1:8000/client/kurslar     => anasayfa



urlpatterns = [   
    path('', views.home),   
    path('list', views.kurslar),
    path('details', views.detay),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobil_uygulamalar),
   
]