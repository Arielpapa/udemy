from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.Pruebaview.as_view()),
    path('lista/',views.PruebaListView.as_view()),
    path('lista_prueba/', views.pruebalista.as_view()),
    path('add/', views.PruebaCreateView.as_view(),name='prueba_add'),
    path('resumen/',views.ResumenFoundation.as_view(),name='resumen'),
]