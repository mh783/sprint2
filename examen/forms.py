from django import forms
from .models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = '__all__'