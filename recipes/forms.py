from django.forms import ModelForm
from recipes.models import Recipe, Playlist

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'picture',
            'description',
        ]

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = [
            'title',
            'picture',
            'recipes',
        ]
