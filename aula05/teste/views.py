from django.shortcuts import render

# Create your views here.
class Produto(models.Model)
    nomeproduto = models.charfield(max_lenght=100)
    preoproduto = models.decimalfield
    descricaoproduto = models.charfield(max _lenght=200)

class cliente(models.model):
    nome = models.chargfield(max_lenght=50)
    sobrenome = models.charfield (max_lenght=50)
    email = models.emailfield
    senha = models.chargfield(nax_length=120)