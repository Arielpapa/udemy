from django.shortcuts import render

#importo TemplateView, ListView y CreateView
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,

)
#importo paquete de urls
from django.urls import reverse_lazy
#importo la clase Empleado que se encuentra en el models.py
from .models import Empleado
#importo el archivo forms.py
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name= 'inicio.html'


# Create your views here.
class ListaAllEmpleados(ListView):
    template_name = 'persona/lista-all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista


class ListaEmpleado(ListView):
    template_name = "persona/listaempleado.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle.html"

    def get_context_data(self,**kwargs):
        context = super (EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context


class Success(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add-lista.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:lista-admin')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:lista-admin')

    def post(self,request,*args,**kwargs):
        self.object= self.get_object()
        print('********metodo post***********')
        print('******************************')
        print(request.POST)
        print(request.POST ['last_name'])
        return super().post(request,*args,**kwargs)

    def form_valid(self,form):
        print('************metodo valid*****')
        return super(EmpleadoUpdateView,self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:lista-admin')

class ListByAreaEmpleado(ListView):
    template_name = 'persona/area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area=self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista-admin.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'empleados'
    