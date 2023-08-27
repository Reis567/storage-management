from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nome

class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='vendedores/', blank=True, null=True)
    

    class Meta:
            verbose_name = "Vendedor"
            verbose_name_plural = "Vendedores"
    def __str__(self):
        return f"Vendedor: {self.user.username}"  # Ou qualquer outra informação que você queira exibir

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
