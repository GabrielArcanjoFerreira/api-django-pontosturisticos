from django.contrib import admin
from comentarios.models import Comentarios

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    pass
