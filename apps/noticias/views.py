from django.shortcuts import render
from .models import Noticia


# Create your views here.
def ListarNoticias(request):
    contexto = {}

    n = Noticia.objects.all() 

    contexto["noticias"] = n

    #print(n)

    #x = Noticia.objects.get(pk=1)

    #print(f"Mi primera noti: {x}")

    return render (request, "noticias/listar.html", contexto)

def DetalleNoticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk = pk)

    contexto["noticia"] = n

    return render (request, "noticias/detalle.html", contexto)
