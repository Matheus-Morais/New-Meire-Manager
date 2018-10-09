from django.db import models

# Create your models here.

class Mensagem(models.Model):
    nome = models.CharField(max_length=100, verbose_name= 'Nome', blank=False)
    email = models.CharField(max_length=200, verbose_name='Email', blank=True)
    telefone = models.IntegerField(verbose_name='Telefone', blank=False)
    mensagem = models.TextField(verbose_name='Mensagem', blank=False)

    def __str__(self):
        return self.nome