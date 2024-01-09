from django import forms
from .models import ModeloBlog

class ModeloBlogFormularfio(forms.ModelForm):
    class Meta:
        model = ModeloBlog
        fields=['autor','titulo','descripcion','imagen']

class ModeloBlogForm(forms.ModelForm):
    class Meta:
        model = ModeloBlog
        fields = ['autor', 'titulo', 'descripcion', 'imagen']

