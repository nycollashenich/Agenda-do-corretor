from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Imovel

class IndexView(TemplateView):
    template_name = 'index.html'

class ImovelListView(ListView):
    model = Imovel
    template_name = 'list.html'
    context_object_name = 'imoveis'

# class ImovelDetailView(DetailView):
#     model = ...
#     template_name = ...
#     context_object_name = ...
