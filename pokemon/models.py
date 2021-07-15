from django.db import models
from django.contrib.auth.models import User


class Pokemon(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    id = models.PositiveIntegerField(unique=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    image = models.ImageField("Изображение покемона", upload_to="pokemon_images/", max_length=255)
    base_happiness = models.PositiveIntegerField()
    capture_rate = models.PositiveIntegerField()
    has_gender_differences = models.BooleanField()
    is_baby = models.BooleanField()
    is_legendary = models.BooleanField()
    is_mythical = models.BooleanField()
    is_playing = models.BooleanField(default=False)
    user = models.ManyToManyField(User, verbose_name="пользователи", related_name="pokemons", blank=True)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('id',)




