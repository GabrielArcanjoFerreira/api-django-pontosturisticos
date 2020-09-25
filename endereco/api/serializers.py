from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco


class EnderecoSerializer(ModelSerializer):
    """ Serializer JSON para o recurso de endereços
    """
    class Meta:
        model = Endereco
        fields = ('id', 'linha1', 'cidade', 'estado', 'pais')