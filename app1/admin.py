from django.contrib import admin
from .models import Persona


#Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display=("nombres","documento")



admin.site.register(Persona,PersonaAdmin)
    


