from django import forms
from .models import Promocao

class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao
        fields = '__all__'
