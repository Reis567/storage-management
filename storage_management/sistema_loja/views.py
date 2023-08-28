from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page

# Create your views here.
def home(request):
    return render(request, 'home.html')



def lista_produtos(request):
    produtos = Produto.objects.all().order_by('tipo__departamento__nome')  # Ordenar por nome do departamento

    paginator = Paginator(produtos, 15)  # Dividir a lista de produtos em páginas de 15 itens cada
    page_number = request.GET.get('page')  # Obter o número da página da query string
    page = paginator.get_page(page_number)  # Obter a página atual
    return render(request, 'lista_produtos.html', 
    {
        'produtos': produtos,
        'page': page,
    })


def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', 
    {
        'produto': produto
    })