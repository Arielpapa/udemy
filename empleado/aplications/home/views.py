from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView

#importo la tabla de model
from .models import prueba

from .forms import PruebaForm

# Create your views here.
class Pruebaview(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundation(TemplateView):
    template_name = 'home/resumen.html'



class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset= ['1','10','20','30']
    context_object_name = 'listanumeros'

class pruebalista(ListView):
    template_name = 'home/lista_prueba.html'
    model = prueba
    context_object_name = 'lista'

    
class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = prueba
   # fields= ['titulo','subtitulo','cantidad']
    form_class = PruebaForm
    success_url = '/'



