from django import forms


class FormularioCrearAerosol(forms.Form):
    
    marca = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    