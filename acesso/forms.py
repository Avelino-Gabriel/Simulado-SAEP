from django import forms
from .models import Professor

class Cad(forms.ModelForm):
    data_nascimento = forms.DateField()

    class Meta:
        model = Professor
        fields = ('email', 'cpf', 'rg', 'data_nascimento', 'sexo')