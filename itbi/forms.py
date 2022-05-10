from django import forms
from .models import Dados

class formulario_processo(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['auditor', 'matricula', 'ano', 'processo_adm', 'objeto_processo', 'cnpj', 'nome_contrib', 'ins_imobiliaria']

class lista_processo(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['processo_adm', 'ano']

class edita_processo(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['auditor', 'matricula', 'objeto_processo', 'cnpj', 'nome_contrib', 'ins_imobiliaria']