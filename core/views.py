import logging

from django.shortcuts import redirect, render
from django.http import HttpResponse

from core.forms import AlunoForm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Aluno
from .serializers import CursoSerializer, AlunoSerializer


def aluno_novo(request):

    if request.method == "POST":
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("aluno_novo")
        else:
            print("Erro", form.errors)
    else:
        form = AlunoForm()
    return render(
        request,
        "aluno_form.html",
        {
            "form": form,
        },
    )


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


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=False, methods=["post"], url_path="matricular")
    def matricular_aluno(self, request):
        aluno_id = request.data.get("aluno_id")
        curso_id = request.data.get("curso_id")

        print(aluno_id)
        print(curso_id)

        if not aluno_id or not curso_id:
            return Response(
                {"erro", "Aluno e Curso são obrigatórios"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            aluno = Aluno.objects.get(id=aluno_id)
        except Aluno.DoesNotExist:
            return Response(
                {"erro": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            curso = Curso.objects.get(id=curso_id)
        except Curso.DoesNotExist:
            return Response(
                {"erro": "Curso não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )

        if aluno.curso == curso:
            return Response(
                {"erro": "Aluno já está matriculado nesse curso"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        aluno.curso = curso
        aluno.save()

        return Response(
            {
                "mensagem": "Matricula realizada com sucesso",
                "aluno": aluno.nome,
                "curso": curso.nome,
            },
            status=status.HTTP_200_OK,
        )

    def get_queryset(self):
        curso = self.request.query_params.get("curso")
        if curso:
            return Aluno.objects.filter(curso=curso)

        return Aluno.objects.all()
