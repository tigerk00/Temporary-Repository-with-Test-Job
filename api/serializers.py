from rest_framework import serializers
from django.contrib.auth.models import User
from pokemon.models import Pokemon


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'email', 'first_name', 'last_name', "pokemons")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["pokemons"] = PokemonSerializer(instance.pokemons.all(), many=True).data
        return rep






class PokemonSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(many=True)

    class Meta:
         model = Pokemon
         fields = ('id', 'name', 'height', 'weight', 'image', 'base_happiness', "capture_rate", "has_gender_differences", "is_baby", "is_legendary", "is_mythical", "user")


