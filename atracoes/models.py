from django.db import models

class Atracao(models.Model):
    """ Modelo para representação das atrações da cidade
    """
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    funcionamento = models.TextField()
    classificacao = models.IntegerField()
    foto = models.ImageField(upload_to='pontosturisticos', null=True, blank=True)

    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"

    def __str__(self):
        """ Representação de um registro de atração no site administrativo
        """
        return self.nome