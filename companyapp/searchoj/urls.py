from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search),
    path('eznetoj/', views.ezsearch),
    path('jsBoj/', views.jsBsearch),
    path('dajoj/', views.dajsearch),
    path('EZB1/', views.ezb1),
    path('EZ1/', views.ez1),
    path('EZ2/', views.ez2),
    path('EZ3/', views.ez3),
    path('EZ4/', views.ez4),
    path('EZ5/', views.ez5),
    path('DAJL/', views.dongajangl),
    path('DAJR/', views.dongajangr),
    path('JB1/', views.jinsungb1),
    path('JB2/', views.jinsungb2),
]
