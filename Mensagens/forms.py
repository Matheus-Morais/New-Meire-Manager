from django import forms
from .models import Mensagem

class MensagemForms(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = '__all__'