from django import forms
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from .models import Vendedor, Departamento
from django.contrib.auth.models import User


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'foto', 'tipo', 'descricao', 'preco', 'quantidade']


class RegistroUsuarioForm(UserCreationForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all())
    foto = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'departamento', 'foto')