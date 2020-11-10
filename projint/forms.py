from django import forms
from .models import Classe

class ClasseForm(forms.ModelForm):
	class Meta:
		model = Classe
		fields = ('nome','descricao', 'detalhe')
