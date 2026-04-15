from django.contrib import admin

from core.models import Aluno, Curso


# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "curso")


admin.site.register(Aluno, AlunoAdmin)

admin.site.register(Curso)
