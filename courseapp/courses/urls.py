from django.urls import path
from . import views

# http://127.0.0.1:8000/client            => anasayfa
# http://127.0.0.1:8000/client/home        => anasayfa
# http://127.0.0.1:8000/client/kurslar     => anasayfa



urlpatterns = [   
    path('', views.home),   
    path('list', views.kurslar),
    path('<kurs_adi>', views.detay),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory, name='getCoursesByCategory'),

]