from django import forms
from .models import Afiliacion, Contacto

class AfiliacionForm(forms.ModelForm):
    class Meta:
        model = Afiliacion
        fields = '__all__'
        


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']
        