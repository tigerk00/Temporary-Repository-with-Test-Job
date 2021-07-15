from django.urls import path
from .views import pokemon_list, user_profile


app_name = "pokemon_app"
urlpatterns = [
    path("list/", pokemon_list, name="pokemon_list"),
    path("profile/", user_profile, name="user_profile"),
]


