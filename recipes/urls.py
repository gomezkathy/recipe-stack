from django.urls import path, include
from recipes.views import show_recipe, recipe_list

urlpatterns = [
    path('recipes/<int:id>/', show_recipe, name='show_recipe'),
    path('recipes/list/', recipe_list, name='recipe_list'),
]
