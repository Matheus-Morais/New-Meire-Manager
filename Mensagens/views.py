from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms import MensagemForms
from .models import Mensagem

def nova_mensagem(request):
    if request.method == 'POST':
        form = MensagemForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            '''send_mail(
                'Nova Mensagem',
                'Você acabou de receber uma nova mensagem de:',
                'matheus.silva.morais01@gmail.com', FROM
                ['matheus.silva.morais01@gmail.com'], TO
                fail_silently=False,
            )'''
            return redirect('contato')
        else:
            print(form.errors)
    else:
        form = MensagemForms()
    return render(request, 'mensagem.html', {'form':form})

@login_required
def lista_mensagens(request):
    if request.user.is_superuser:
        mensagens = Mensagem.objects.all()
        return render(request, 'lista_mensagens.html', {'mensagens': mensagens})
    else:
        return redirect('error-404')

@login_required
def delete_mensagem(request, id):
    if request.user.is_superuser:
        mensagem = Mensagem.objects.get(pk=id)
        mensagem.delete()
        return redirect('msg:lista-mensagens')
    else:
        return redirect('error-404')