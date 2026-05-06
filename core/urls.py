from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import AlunoViewSet, CursoViewSet

router = DefaultRouter()

router.register("cursos", CursoViewSet)
router.register("alunos", AlunoViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
