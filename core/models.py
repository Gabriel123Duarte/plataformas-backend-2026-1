from django.db import models


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default="teste@teste.com")
    idade = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
