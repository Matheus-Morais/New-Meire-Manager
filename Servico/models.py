from django.db import models

# Create your models here.

class Servico(models.Model):
    TIPO_CHOICES = (
        ('M', 'Manicure'),
        ('P', 'Pédicure'),
        ('C', 'Cabelo'),
        ('S', 'Sobrancelha'),
        ('MA', 'Maquiagem'),
    )
    servico = models.CharField(max_length=100, verbose_name= 'Servico', blank=False)
    valor_minimo = models.CharField(max_length=4, verbose_name='Valor_minimo', blank=False)
    valor_maximo = models.CharField(max_length=4, verbose_name='Valor_maximo', blank=False)
    tipo = models.CharField(verbose_name='Tipo', max_length=2, choices=TIPO_CHOICES, blank=False)
    imagem = models.CharField(verbose_name='Imagem', max_length=1000, blank=True)
    descrição = models.TextField(verbose_name='Descrição', blank=True)
    desconto = models.BooleanField(verbose_name='Desconto', default=False, blank=True)
    valor_desconto = models.IntegerField(verbose_name='Valor Desconto', default=0, blank=True)

    def __str__(self):
        return self.servico