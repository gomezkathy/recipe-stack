from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, PlaylistForm
from django.contrib.auth.models import User

@login_required
def create_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.created_by = request.user
            playlist.save()
            return redirect("recipe_list")
    else:
        form = PlaylistForm()
        form.fields['recipes'].queryset = Recipe.objects.filter(created_by=request.user)

    context = {
        "form": form,
    }

    return render(request, "recipes/create_playlist.html", context)


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe_object': recipe,
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_list(request):
    user = request.user
    recipes = Recipe.objects.filter(created_by=user)
    context = {
        'recipe_list': recipes,
    }
    return render(request, 'recipes/list.html', context)

@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }

    return render(request, "recipes/create.html", context)
