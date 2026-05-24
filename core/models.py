from django.db import models


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(default=0)

    def __str__(self):
        return self.nome + " " + self.carga_horaria


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default="teste@teste.com")
    idade = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
