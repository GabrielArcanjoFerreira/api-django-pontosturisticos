from django.contrib import admin
from atracoes.models import Atracao

@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    pass
