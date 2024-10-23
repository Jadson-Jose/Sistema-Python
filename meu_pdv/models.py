from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, through='ItemVenda')


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
