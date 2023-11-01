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
        labels = {
            'title': 'Enter Title',
            'picture': 'Picture Url',
        }

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['title', 'picture', 'recipes']
        labels = {
            'title': 'Enter Title',
            'picture': 'Picture Url',
        }

    recipes = forms.ModelMultipleChoiceField(
        queryset=Recipe.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select From Your Recipes Below',
    )
