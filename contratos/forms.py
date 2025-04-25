from django import forms
from .models import Contrato, ArchivoAdjunto

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['tipo', 'titulo', 'parte_a', 'parte_b', 'fecha_inicio', 'fecha_fin', 'descripcion']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

class ArchivoAdjuntoForm(forms.ModelForm):
    class Meta:
        model = ArchivoAdjunto
        fields = ['nombre', 'archivo']