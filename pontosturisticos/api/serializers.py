from rest_framework.serializers import ModelSerializer
from pontosturisticos.models import PontosTuristicos
from atracoes.api.serializers import AtracaoSerializerNested


class PontoTuristicoSerializer(ModelSerializer):
    """ Serializador JSON para o recurso de pontos turisticos
    """
    atracoes = AtracaoSerializerNested(many=True)

    class Meta:
        model = PontosTuristicos
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'descricao_complete')