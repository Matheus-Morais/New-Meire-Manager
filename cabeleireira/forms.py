from django import forms
from .models import Cabeleireira, Cabeleireira_Servico

class CabeleireiraForm(forms.ModelForm):
    class Meta:
        model = Cabeleireira
        fields = '__all__'

class Cabeleireira_ServicoForm(forms.ModelForm):
    class Meta:
        model = Cabeleireira_Servico
        fields = '__all__'