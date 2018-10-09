from django.db import models
from django.contrib.auth.models import User
from Accounts.models import Usuario
from cabeleireira.models import Cabeleireira_Servico

# Create your models here.

class Agendar(models.Model):
    STATUS_CHOICES = (
        ('SO', 'Solicitado'),
        ('CO', 'Confirmado'),
        ('EA', 'Em Andamento'),
        ('C', 'Concluido'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cabeleireira_servico = models.ForeignKey(Cabeleireira_Servico, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=False, auto_now_add=False, unique=True, blank=False)
    status = models.CharField(verbose_name='Status', max_length=2, choices=STATUS_CHOICES, default='SO')

    def __str__(self):
        return 'Cliente: '+self.cliente.user.get_full_name() + ' - Serviço: ' + self.cabeleireira_servico.servico.servico