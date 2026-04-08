import logging

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    if request.method == "POST":
        nome = request.POST.get("nome")

        if not nome:
            return HttpResponse("Preencha seu nome")

        nome = nome.strip()

        logger = logging.getLogger(__name__)
        logger.warning("Nome digitado foi" + nome)

        if len(nome) < 3:
            return HttpResponse("O nome tem que ter pelo menos 3 caracteres")

        return HttpResponse(nome)

    elif request.method == "GET":
        return render(request, "homepage.html")
    elif request.method == "PUT":
        return HttpResponse("Método PUT não permitido")
    else:
        return HttpResponse("Método desconhecido")
