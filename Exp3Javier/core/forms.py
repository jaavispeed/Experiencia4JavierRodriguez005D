from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['rut','nombre','producto']
        labels ={
            'rut': 'Rut', 
            'nombrec': 'Nombre',
            'producto': 'producto', 
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombrec': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombrec'
                }
            )
        }