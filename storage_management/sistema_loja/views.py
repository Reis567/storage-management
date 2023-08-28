from django.shortcuts import render
from .models import Produto
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def lista_produtos(request):
    user = request.user

    if user.is_superuser:
        # Se o usuário é um superusuário (gerência), mostrar todos os produtos
        produtos = Produto.objects.all().order_by('tipo__departamento__nome')
    elif user.vendedor:
        # Se o usuário é um vendedor, filtrar os produtos pelo departamento do vendedor
        departamento_vendedor = user.vendedor.departamento
        produtos = Produto.objects.filter(tipo__departamento=departamento_vendedor).order_by('nome')
    else:
        produtos = Produto.objects.none()  # Se nenhum vendedor ou gerência, não mostrar produtos


    paginator = Paginator(produtos, 15)  # Dividir a lista de produtos em páginas de 15 itens cada
    page_number = request.GET.get('page')  # Obter o número da página da query string
    page = paginator.get_page(page_number)  # Obter a página atual
    return render(request, 'lista_produtos.html', 
    {
        'produtos': produtos,
        'page': page,
    })

@login_required
def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', 
    {
        'produto': produto
    })