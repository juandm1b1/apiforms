# Sitio web: Formulario para agregar nombre y q se almacene en BD

from django import forms
from .models import Persona

class Form_nombre(forms.Form):
    nombre = forms.CharField(label='', max_length=100)



class ContactForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)
    remitente = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)  


HOBBIES = [
    ('escuchar música','Escuchar música'),
    ('leer', 'Leer'),
    ('escribir','Escribir'),
    ('pintar','Pintar'),
    ]

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude = ['hobbies']
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

  # hobbies = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=HOBBIES)


class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=10)
    contrasena = forms.CharField(max_length=15)



"""1. arreglar urls con include o mas bien modularización


#arreglar para que sí envíe mail
#que no se vea el formulario en un mismo renglón"""