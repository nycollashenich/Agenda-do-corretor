from django.urls import path
from .views import IndexView, ImovelListView, CreateImovelView, UpdateImovelView, DeleteImovelView, DetailImovelView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listadeimoveis/', ImovelListView.as_view(), name='list'),
    path('adicionarimovel/', CreateImovelView.as_view(), name='add_imovel'),
    path('<slug:slug>/atualizarimovel/', UpdateImovelView.as_view(), name='upd_imovel'),
    path('<slug:slug>/deletarimovel/', DeleteImovelView.as_view(), name='del_imovel'),
    path('<slug:slug>/detalheimovel/', DetailImovelView.as_view(), name='detalhe_imovel')

]
