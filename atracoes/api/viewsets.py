from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    """ View para o recurso de atrações
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao')