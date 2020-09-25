from django.contrib import admin
from pontosturisticos.models import PontosTuristicos

@admin.register(PontosTuristicos)
class PontosTuristicosAdmin(admin.ModelAdmin):
    pass
