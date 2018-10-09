from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, verbose_name= 'CPF', blank=False)
    rg = models.CharField(max_length=7, verbose_name='RG', blank=False)
    telefone = models.CharField(max_length=12,verbose_name='Telefone', blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()