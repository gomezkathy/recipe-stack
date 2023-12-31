from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, create_playlist, playlist_list, show_playlist, show_playlist_recipes, edit_recipe, delete_recipe, edit_playlist, delete_playlist

urlpatterns = [
    path('recipes/<int:id>/', show_recipe, name='show_recipe'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/create/', create_recipe, name='create_recipe'),
    path('recipes/edit/<int:id>/', edit_recipe, name='edit_recipe' ),
    path('recipes/delete/<int:id>/', delete_recipe, name='delete_recipe'),
    path('recipes/create_playlist/', create_playlist, name='create_playlist'),
    path('recipes/playlists/', playlist_list, name='playlist_list'),
    path('recipes/edit_playlist/<int:playlist_id>/', edit_playlist, name='edit_playlist' ),
    path('recipes/delete_playlist/<int:playlist_id>/', delete_playlist, name='delete_playlist'),
    path('recipes/playlists/<int:id>/', show_playlist, name='show_playlist'),
    path('recipes/playlists/<int:playlist_id>/recipes/', show_playlist_recipes, name='show_playlist_recipes'),
]
