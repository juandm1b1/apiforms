from django.contrib.postgres.fields import ArrayField
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Nombre(models.Model):

    nombre = models.CharField(max_length=40)

    def __str__(self):

        return self.nombre



class Contacto(models.Model):

    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    remitente = models.EmailField()    
    cc_myself = models.BooleanField()  

    def __str__(self):
        return self.asunto



HOBBIES = [
    ('escuchar música','Escuchar música'),
    ('leer', 'Leer'),
    ('escribir','Escribir'),
    ('pintar','Pintar'),
    ]

class Persona(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)    
    documento = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    hobbies = MultiSelectField(choices=HOBBIES, null= True, blank= True)
    #hobbies = ArrayField(models.CharField(max_length=50))    

    def __str__(self):
        return self.nombres, self.apellidos



class Login(models.Model):
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=10)
    contrasena = models.CharField(max_length=10)

# def __str__(self):
#         return Persona.nombres(id_persona)

