from django.forms import ModelForm
from recipes.models import Recipe, Playlist
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'picture',
            'description',
            'instructions',
        ]

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'picture', 'recipes']

    recipes = forms.ModelMultipleChoiceField(
        queryset=Recipe.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
