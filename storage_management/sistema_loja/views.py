from django.shortcuts import render,redirect
from .models import Produto, TipoProduto
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from django.contrib import messages

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
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('detalhes_produto', produto_id=produto_id)
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'detalhes_produto.html', {
        'produto': produto,
        'form': form,
    })


@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            novo_produto = form.save()  # Salvar o produto e obter o objeto criado
            produto_id = novo_produto.id  # Obter o ID do produto criado
            return redirect('detalhes_produto', produto_id=produto_id)  # Redirecionar para a página de detalhes
    else:
        form = ProdutoForm()
    
    return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return redirect('detalhes_produto', produto_id=produto_id)


