from django.shortcuts import render

def Home(request):

    return render(request, 'home.html')


def Pruebas(request):
                                # este def es de andres jugando un poco nomas
    return render(request, 'pruebas.html') 


def contacto(request):
                                # este def es de la pagina de contacto
    return render(request, 'contacto.html') 