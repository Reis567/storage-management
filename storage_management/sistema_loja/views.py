from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'home.html')



def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', 
    {
                'produtos': produtos
    })


def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', 
    {
        'produto': produto
    })