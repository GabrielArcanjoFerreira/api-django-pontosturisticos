from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacoes


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = '__all__'