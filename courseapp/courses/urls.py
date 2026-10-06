from django.urls import path
from . import views

# http://127.0.0.1:8000/client            => anasayfa
# http://127.0.0.1:8000/client/home        => anasayfa
# http://127.0.0.1:8000/client/kurslar     => anasayfa



urlpatterns = [   
    path('', views.index, name='index'),  
    path('search', views.search, name='search'),
    path('create-kurs', views.create_kurs, name='create_course'),
    path('course-list', views.course_list, name='course_list'),
    path('course_edit/<slug:slug>', views.course_edit, name='course_edit'),
    path('course_delete/<slug:slug>', views.course_delete, name='course_delete'),
    path('<slug:slug>', views.detay, name='course_details'),
    path('kategori/<slug:slug>',views.getCoursesByCategory, name='getCoursesByCategory'),
    

]