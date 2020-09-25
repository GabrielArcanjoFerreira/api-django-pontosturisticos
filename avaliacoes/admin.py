from django.contrib import admin
from avaliacoes.models import Avaliacoes

@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    pass