from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante, informacoes_visitante, finalizar_visita

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("registrar_visitante/", registrar_visitante, name="registrar_visitante"),
    path("visitantes/<int:id>/", informacoes_visitante, name="informacoes_visitante"),
    path("visitantes/<int:id>/finalizar_visita/", finalizar_visita, name="finalizar_visita"),
]
