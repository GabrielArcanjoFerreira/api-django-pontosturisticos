from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    """ View para acesso do recurso de comentários
    """
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer