from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    
    #Futuramente colocar :
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ainda não é possivel colocar o vendedor por nao ter um sistema de login desenvolvido 

    def __str__(self):
        return f"Vendedor do {self.departamento}"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
