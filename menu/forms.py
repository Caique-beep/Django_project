from django.contrib.auth.forms import forms
from menu.models import Sabores, Massa, TamanhoPizza


class SabooresForm(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    ingredientes = forms.CharField(max_length=200)

    class Meta:
        model = Sabores
        fields = ['nome', 'ingredientes']


class MassaForm(forms.ModelForm):
    tipo = forms.CharField(max_length=20)

    class Meta:
        model = Massa
        fields = ['tipo']


class TamanhoForm(forms.ModelForm):
    tamanho = forms.CharField(max_length=20)

    class Meta:
        model = TamanhoPizza
        fields = ['tamanho']