from rest_framework import viewsets
from django.contrib.auth.models import User
from pokemon.models import Pokemon
from .serializers import PlayerSerializer, PokemonSerializer
from .permissions import IsPlayerOrReadOnly



class PlayerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsPlayerOrReadOnly,]


class PokemonViewSet(viewsets.ModelViewSet):
        queryset = Pokemon.objects.all()
        serializer_class = PokemonSerializer
        lookup_field = 'id'


