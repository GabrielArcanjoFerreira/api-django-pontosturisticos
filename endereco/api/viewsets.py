from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    """ View para retorno do recurso de endereços
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer