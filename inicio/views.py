from django.shortcuts import render

# Create your views here.

def inicial (request):
    contexto = {


    }
    return render(request, 'inicio.html', contexto)