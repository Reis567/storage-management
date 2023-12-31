from django.contrib import admin
from .models import Departamento, TipoProduto, Vendedor, Produto

# Register your models here.

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'departamento')

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'departamento')
    list_filter = ('departamento',)

    def display_name(self, obj):
        return obj.user.username
    
    display_name.short_description = 'Nome do Vendedor'

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'preco', 'quantidade')
    list_filter = ('tipo__departamento', 'tipo')
