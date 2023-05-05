from django.forms import ModelForm
from .models import Pacientes
from django import forms

class PacientesForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = [
            "nombre",
            "apellido",
            "peso",
            "sexo",
            "estado"
        ]
        labels = {
           "nombre": "Nombre"
        } 
        widgets = {
            'nombre': forms.TextInput(
            attrs={
                "class": "form-control"
            }
            )
            
        }