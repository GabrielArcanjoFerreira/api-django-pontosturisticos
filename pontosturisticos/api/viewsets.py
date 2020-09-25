from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from pontosturisticos.models import PontosTuristicos
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """ View para o recurso de pontos turisticos
    """
    # queryset = PontosTuristicos.objects.all()
    serializer_class = PontoTuristicoSerializer
    http_method_names = ['delete', 'post', 'get', 'put', 'patch']
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    # lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id')
        nome = self.request.query_params.get('nome')
        descricao = self.request.query_params.get('descricao')

        queryeset = PontosTuristicos.objects.all()

        if id:
            queryeset = queryeset.filter(id=id)
        if nome:
            queryeset = queryeset.filter(nome__iexact=nome)
        if descricao:
            queryeset = queryeset.filter(descricao__iexact=descricao)

        return queryeset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def testar(self, request):
        pass