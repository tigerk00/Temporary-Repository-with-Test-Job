from rest_framework.routers import SimpleRouter
from .views import PlayerViewSet, PokemonViewSet


router = SimpleRouter()
router.register('players', PlayerViewSet, basename='players')
router.register('pokemons', PokemonViewSet, basename='pokemons')

urlpatterns = router.urls

