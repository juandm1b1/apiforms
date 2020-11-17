# Sitio web: Formulario para agregar nombre y q se almacene en BD

from django import forms
from .models import Persona
from django.contrib.postgres.forms import SimpleArrayField
from multiselectfield import MultiSelectFormField

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
    #fecha_nacimiento = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)  
    
    class Meta:
        model = Persona
        #exclude = ['hobbies']
        fields = '__all__'
        widgets = {
                    'hobbies': forms.CheckboxSelectMultiple(choices=HOBBIES),
                    'fecha_nacimiento': forms.DateInput(),
                    }

  # hobbies = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=HOBBIES)

  # 'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'},)
