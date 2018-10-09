from django.db import models
from Servico.models import Servico

# Create your models here.

class Cabeleireira(models.Model):
    nome = models.CharField(max_length=200, verbose_name= 'Nome', blank=False)
    numero = models.CharField(max_length=11, verbose_name='Numero de telefone', blank=False)
    trabalhos_realizados = models.IntegerField(verbose_name='Trabalhos realizadaos', default=0, blank=True)

    def __str__(self):
        return self.nome

class Cabeleireira_Servico(models.Model):
    cabeleireira = models.ForeignKey (Cabeleireira, on_delete=models.CASCADE)
    servico = models.OneToOneField (Servico, on_delete=models.CASCADE)

    def __str__(self):
        return self.cabeleireira.nome + ' - ' + self.servico.servico
