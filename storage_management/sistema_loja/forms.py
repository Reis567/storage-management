from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'foto', 'tipo', 'descricao', 'preco', 'quantidade']
