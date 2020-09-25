from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    """ Classe para serialização JSON do recurso de atrações
    """
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'foto', 'funcionamento', 'classificacao')

class AtracaoSerializerNested(ModelSerializer):
    """ Classe para serialização JSON do recurso de atrações
    """
    class Meta:
        model = Atracao
        fields = ('nome',)