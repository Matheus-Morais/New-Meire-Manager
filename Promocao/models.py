from django.db import models
from Servico.models import Servico

# Create your models here.

class Promocao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name= 'Titulo', blank=False)
    descrição = models.TextField(verbose_name='Descrição', blank=True)
    servico = models.ManyToManyField(Servico)
    valor_minimo = models.CharField(max_length=4, verbose_name='Valor_minimo', blank=False)
    valor_maximo = models.CharField(max_length=4, verbose_name='Valor_maximo', blank=False)
    imagem = models.CharField(verbose_name='Imagem', max_length=1000, blank=True)
    valor_desconto = models.IntegerField(verbose_name='Valor Desconto', default=0, blank=True)

    def __str__(self):
        return self.titulo