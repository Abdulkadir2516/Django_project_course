from django.urls import path
from . import views

# http://127.0.0.1:8000/client            => anasayfa
# http://127.0.0.1:8000/client/home        => anasayfa
# http://127.0.0.1:8000/client/kurslar     => anasayfa



urlpatterns = [   
    path('', views.index),   
    path('<slug:slug>', views.detay, name='course_details'),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name='getCoursesByCategory'),
    path('search/', views.search, name='search'),

]