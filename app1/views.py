from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate
#from django.contrib.auth.views import login, logout_then_login #Para traer login y logout por defecto

from .forms import Form_nombre, ContactForm, PersonaForm
from .models import Nombre, Contacto, Persona, Login


from django.core.mail import send_mail


def bienvenida(request):

    cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]

    lista = [
        {'animal':'perro', 'categoria': 'doméstico'}, 
        {'animal': 'gato', 'categoria': 'doméstico'}, 
        {'animal': 'ballena', 'categoria': 'silvestre'},
        {'animal': 'lobo', 'categoria': 'silvestre'},
        {'animal': 'águila', 'categoria': 'silvestre'},
        {'animal': 'gallina', 'categoria': 'doméstico'},
        ]

    telefono = "abcdefghijklmnñopqrstuvwxyz"
    fecha = "01:23"
        
    return render(request, "app1/bienvenida.html", {'cities': cities, 'lista': lista, 'telefono': telefono, 'fecha': fecha})


class FormularioRegistroView(HttpResponse):

    def verRegistros(request):
        registros = Persona.objects.all()
        return render(request, "app1/lista_registros.html", {'registros': registros})


    def crearRegistro(request):

        if request.method == "POST":
            
            fregistro = PersonaForm(request.POST) #Se intancia form RegistroForm            

            if fregistro.is_valid():

                infRegistro = fregistro.cleaned_data #Si form es válido se obtienen datos limpios          

                lista_hobbies=[]
                

                hobbis=infRegistro['hobbies']


                for hobbi in hobbis:
                    lista_hobbies.append(hobbi)            
                        

                #Se instancia model Persona
                bdRegistro = Persona(nombres=infRegistro['nombres'], apellidos=infRegistro['apellidos'], documento=infRegistro['documento'],
                        fecha_nacimiento=infRegistro['fecha_nacimiento'],telefono=infRegistro['telefono'],email=infRegistro['email'],hobbies=lista_hobbies)            
                
                

                buscar_registro = Persona.objects.filter(documento=bdRegistro.documento).count() #Cuenta registros en BD que coinciden con el doc ingresado en el form

                if buscar_registro==0:

                    bdRegistro.save() 

                else:

                    messages.error(request, 'Ya existe un registro con este número de documento.')               
                    
                    return render(request, "app1/registro.html")
                
                
                registros = Persona.objects.all()            
                

                ctx = {"registros": registros}  


                return render(request, 'app1/lista_registros.html', ctx)           

        else:

            fregistro = PersonaForm()            
             

        return render(request, 'app1/registro.html')


    def eliminarRegistro(request, id_persona):
        
        reg_a_eliminar = Persona.objects.get(pk=id_persona)
        reg_a_eliminar.delete()
        registros = Persona.objects.all()   
        ctx = {"registros": registros} 

        return render(request, 'app1/lista_registros.html', ctx)



    def editarRegistro(request, id_persona):
        
        reg_a_editar = Persona.objects.get(pk=id_persona)
        #return HttpResponse(reg_a_editar.telefono)
        formu = PersonaForm(instance=reg_a_editar)

        if request.method == "POST":
            form2 = PersonaForm(request.POST, instance = reg_a_editar)

            if form2.is_valid():

                form2.save()

                # infRegistro = form2.cleaned_data #Si form es válido se obtienen datos limpios          

                # lista_hobbies=[]
                

                # hobbis=infRegistro['hobbies']


                # for hobbi in hobbis:
                #     lista_hobbies.append(hobbi)            
                        

                # #Se instancia model Persona
                # bdRegistro = reg_a_editar(nombres=infRegistro['nombres'], apellidos=infRegistro['apellidos'], documento=infRegistro['documento'],
                #         fecha_nacimiento=infRegistro['fecha_nacimiento'],telefono=infRegistro['telefono'],email=infRegistro['email'],hobbies=lista_hobbies)

                
                # bdRegistro.save()

                registros = Persona.objects.all()

                ctx = {'registros': registros}

                return render(request, "app1/lista_registros.html", ctx)


        ctx = {'formu': formu, 'reg_a_editar': reg_a_editar}
        return render(request, "app1/experimento.html", ctx)





# def login(request):

#     if request.method == "POST":
        
#         fLogin = LoginForm(request.POST)  
#         #countr = 0      

#         if fLogin.is_valid():            

#             infLogin = fLogin.cleaned_data

#             user = authenticate(username=infLogin['usuario'], password=infLogin['contrasena'])

#             if user is not None:
#                 messages.success(request, user.first_name)                
#                 registros = Persona.objects.all()
#                 return render(request, "app1/lista_registros.html", {"user": user, "registros": registros})
#             else:
#                 messages.error(request, 'No existe ningún registro con este usuario')            

#     else:
#         fLogin = LoginForm()


#     return render(request, 'app1/login.html')    






# def Form_contacto(request):

#     if request.method == "POST":

#         form = ContactForm(request.POST) 

#         if form.is_valid():
#             formulario = form.cleaned_data
#             asunto = form.cleaned_data['asunto']
#             mensaje = form.cleaned_data['mensaje']
#             remitente = form.cleaned_data['remitente']            
#             cc_myself = form.cleaned_data['cc_myself']
            

#             bdcontacto = Contacto(asunto=asunto, mensaje=mensaje, remitente=remitente, cc_myself=cc_myself)

#             bdcontacto.save()   

#         destinatario = ["soundgar@yahoo.es"]

#         if cc_myself:
#             destinatario.append(remitente)
#             send_mail(asunto, mensaje, remitente, destinatario)

        

#         bdregistros = Contacto.objects.all()

#         return render(request, "app1/contactos.html", {"formulario": formulario, "bdregistros": bdregistros})

#     else:
        
#         form = ContactForm()
        

#     return render(request, "app1/form_contacto.html", {"form": form})



# def nombre(request):

#     if request.method == "POST":
        
#         fnombre = Form_nombre(request.POST)

#         if fnombre.is_valid():

#             inffnombre = fnombre.cleaned_data            

#             bdnombre = Nombre(nombre=inffnombre['nombre'])

#             bdnombre.save()

#             nombres = Nombre.objects.all()

#             total_nombres = nombres.count()
#             contnombre = Nombre.objects.filter(nombre=bdnombre).count()    

#             ctx = {"bdnombre": bdnombre, "nombres": nombres, "total_nombres": total_nombres, "contnombre": contnombre}  


#             return render(request, 'app1/listanombres.html', ctx)           

#     else:

#         fnombre = Form_nombre()     

#     return render(request, 'app1/name.html', {"fnombre": fnombre})