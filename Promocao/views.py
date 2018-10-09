from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Promocao
from .forms import PromocaoForm

from Servico.models import Servico

# Create your views here.

def lista_promocoes(request):
    promocoes = Servico.objects.filter(desconto=True)
    if promocoes:   
    # promocoes = promocoes.servico.all()
    # return redirect('em-andamento')
        return render(request, 'lista_promocoes.html', {'promocoes': promocoes})
    else:
        return redirect('em-andamento')

@login_required
def add_promocao(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PromocaoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Promoção criada com Sucesso!')
                return redirect('promoções:nova-promocao')
            else:
                messages.error(request, form.errors)
        else:
            form = PromocaoForm()
        return render(request, 'add_promocao.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def update_promocao(request, id):
    if request.user.is_superuser:
        promocao = Promocao.objects.get(id=id)
        if request.method == 'POST':
            form = PromocaoForm(data=request.POST, instance=promocao)
            if form.is_valid():
                form.save()
                messages.success(request, 'Promoção editada com Sucesso!')
                return redirect('promoções:editar-promocao', id)
            else:
                messages.error(request, form.errors)
        else:
            form = PromocaoForm(instance=promocao)
        return render(request, 'add_promocao.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def delete_promocao(resquest, id):
    if resquest.user.is_superuser:
        promocao = Promocao.objects.get(id=id)
        promocao.delete()
        return redirect('promoções:nova-promocao')
    else:
        return redirect('error-404')