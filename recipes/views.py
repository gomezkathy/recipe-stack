from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.contrib.auth.decorators import login_required

def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe_object': recipe,
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipe_list': recipes,
    }
    return render(request, 'recipes/list.html', context)
