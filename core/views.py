from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Imovel
from .forms import ImovelModelForm
from django.urls import reverse_lazy 

class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class DetailImovelView(DetailView):
    model = Imovel
    template_name = 'imovel_detalhe.html'
    context_object_name = 'imoveis'
    slug_field = 'slug'

class ImovelListView(ListView):
    model = Imovel
    template_name = 'list.html'
    queryset = Imovel.objects.all()
    context_object_name = 'imoveis'

class CreateImovelView(CreateView):
    model = Imovel
    template_name = 'imovel_form.html'
    fields = ['tipo', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'agenda','num_quartos', 'num_banheiros', 'num_garagem', 'pets', 'condicoes', 'proprietario', 'descricao']
    success_url = reverse_lazy('list')
    slug_field = 'slug'

class UpdateImovelView(UpdateView):
    model = Imovel
    template_name = 'imovel_form.html'
    fields = ['rua', 'numero', 'bairro', 'cidade', 'estado', 'condicoes', 'agenda']
    success_url= reverse_lazy('list')
    slug_field = 'slug'

class DeleteImovelView(DeleteView):
    model = Imovel
    template_name = 'imovel_del.html'
    success_url = reverse_lazy('list')

