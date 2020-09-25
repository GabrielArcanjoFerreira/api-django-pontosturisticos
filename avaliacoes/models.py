from django.db import models
from django.contrib.auth.models import User


class Avaliacoes(models.Model):
    """ Modelo para representação das avaliações de cada usuario
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        """ Representação de um registro no portal de administração
        """
        return f'{self.usuario.first_name} {self.usuario.last_name} - {self.avaliacao} estrelas'