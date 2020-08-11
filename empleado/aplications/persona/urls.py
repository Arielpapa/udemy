from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '',views.InicioView.as_view(),
        name='inicio'
    ),
    path(
        'lista-all/',
        views.ListaAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'detalle-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='detalle-empleado'
    ),
    path('buscarempleado/',views.ListaEmpleado.as_view()),
    path(
        'all-lista/' ,
        views.EmpleadoCreateView.as_view(),
        name='registrar-empleado'
    ),
    path(
        'success/',
        views.Success.as_view(),
        name='correcto'
        ),
    path(
        'update/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar'
    ),
    path(
        'delete/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar'
    ),
    path(
        'lista-area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name='lista-area'
    ),
    path(
        'lista-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='lista-admin'
    ),


]
