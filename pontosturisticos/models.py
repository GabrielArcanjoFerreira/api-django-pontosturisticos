from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacoes
from comentarios.models import Comentarios
from endereco.models import Endereco

class PontosTuristicos(models.Model):
    """ Modelo para representação dos pontos turísticos
    """
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontosturisticos', null=True, blank=True)

    class Meta:
        verbose_name = 'Ponto Turístico'
        verbose_name_plural = 'Pontos Turísticos'

    @property
    def descricao_complete(self):
        return f'{self.nome} - {self.descricao}'

    def __str__(self):
        """ String para representação de registros no site de administração
        """
        return self.nome

