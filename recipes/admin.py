from django.contrib import admin
from recipes.models import Recipe, Playlist

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
    ]

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
    ]
