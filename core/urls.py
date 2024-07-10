from django.urls import path
from .views import IndexView, ImovelListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lista/', ImovelListView.as_view(), name='list'),
    # path('listadetalhe/', ImovelDetailView.as_view(), name='listdetail')
]
