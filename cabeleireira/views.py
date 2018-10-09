from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Cabeleireira, Cabeleireira_Servico
from .forms import CabeleireiraForm, Cabeleireira_ServicoForm

##########################################
#Cabeleireira#
##########################################

@login_required
def lista_cabeleireira(request):
    if request.user.is_superuser:
        cabeleireiras = Cabeleireira.objects.all()
        return render(request, 'lista_cabeleireira.html', {'cabeleireiras': cabeleireiras})
    else:
        return redirect('error-404')

@login_required
def add_cabeleireira(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CabeleireiraForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cabeleireira criada com Sucesso!')
                return redirect('cabeleireira:lista-cabeleireira')
            else:
                messages.error(request, form.errors)
        else:
            form = CabeleireiraForm()
        return render(request, 'add_cabeleireira.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def update_cabeleireira(request, id):
    if request.user.is_superuser:
        cabeleireira = Cabeleireira.objects.get(id=id)
        if request.method == 'POST':
            form = CabeleireiraForm(data=request.POST, instance=cabeleireira)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cabeleireira editada com Sucesso!')
                return redirect('cabeleireira:lista-cabeleireira')
            else:
                messages.error(request, form.errors)
        else:
            form = CabeleireiraForm(instance=cabeleireira)
        return render(request, 'add_cabeleireira.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def delete_cabeleireira(resquest, id):
    if resquest.user.is_superuser:
        cabeleireira = Cabeleireira.objects.get(id=id)
        cabeleireira.delete()
        return redirect('cabeleireira:lista-cabeleireira')
    else:
        return redirect('error-404')

##########################################
#Fim Cabeleireira#
##########################################

##########################################
#Cabeleireira_Serviço#
##########################################
@login_required
def lista_servicos_cabeleireira(request, id):
    if request.user.is_superuser:
        cabeleireira = Cabeleireira.objects.get(id=id)
        nome = cabeleireira.nome
        cabeleireira_servico = Cabeleireira_Servico.objects.filter(cabeleireira=cabeleireira)
        return render(request, 'lista_servicos_cabeleireira.html', {'cabeleireira_servico': cabeleireira_servico, 'nome': nome})
    else:
        return redirect('error-404')

@login_required
def add_servicos_cabeleireira(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Cabeleireira_ServicoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Serviço atribuido para cabeleireira com Sucesso!')
                return redirect('cabeleireira:lista-cabeleireira')
            else:
                messages.error(request, form.errors)
        else:
            form = Cabeleireira_ServicoForm()
        return render(request, 'add_servico_cabeleireira.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def update_servico_cabeleireira(request, id):
    if request.user.is_superuser:
        cabeleireira_servico = Cabeleireira_Servico.objects.get(id=id)
        if request.method == 'POST':
            form = Cabeleireira_ServicoForm(data=request.POST, instance=cabeleireira_servico)
            if form.is_valid():
                form.save()
                messages.success(request, 'Serviço da cabeleireira editado com Sucesso!')
                return redirect('cabeleireira:lista-cabeleireira')
            else:
                messages.error(request, form.errors)
        else:
            form = Cabeleireira_ServicoForm(instance=cabeleireira_servico)
        return render(request, 'add_servico_cabeleireira.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def delete_servico_cabeleireira(resquest, id):
    if resquest.user.is_superuser:
        cabeleireira_servico = Cabeleireira_Servico.objects.get(id=id)
        id_cab = cabeleireira_servico.cabeleireira.id
        cabeleireira_servico.delete()
        return redirect('cabeleireira:lista-servico-cabeleireira', id_cab)
    else:
        return redirect('error-404')

##########################################
#Fim Cabeleireira_Serviço#
##########################################
