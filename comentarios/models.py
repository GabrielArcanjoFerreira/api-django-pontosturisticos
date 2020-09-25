from django.db import models
from django.contrib.auth.models import User


class Comentarios(models.Model):
    """ Modelo para representação dos comentários de cada usuário
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ocultar = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        """ Representação no site de adminsitração
        """
        return f'{self.usuario.first_name} {self.usuario.last_name} - {self.data_publicacao}'

