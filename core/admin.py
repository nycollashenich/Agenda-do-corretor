from django.contrib import admin
from .models import Imovel

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'rua', 'estado', 'cidade']
    prepopulated_fields = {'slug': ('rua',)}
