from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, create_playlist, playlist_list, show_playlist

urlpatterns = [
    path('recipes/<int:id>/', show_recipe, name='show_recipe'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/create/', create_recipe, name='create_recipe'),
    path('recipes/create_playlist/', create_playlist, name='create_playlist'),
    path('recipes/playlists/', playlist_list, name='playlist_list'),
    path('recipes/playlists/<int:id>/', show_playlist, name='show_playlist'),
]
