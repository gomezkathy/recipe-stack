from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Playlist
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, PlaylistForm
from django.contrib.auth.models import User


def show_playlist_recipes(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    recipes = playlist.recipes.all()

    context = {
        'playlist': playlist,
        'recipes': recipes,
    }
    return render(request, 'recipes/playlist_recipes.html', context)

@login_required
def create_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.created_by = request.user
            playlist.save()
            form.save_m2m()
            return redirect("recipe_list")
    else:
        form = PlaylistForm()
        form.fields['recipes'].queryset = Recipe.objects.filter(created_by=request.user)

    context = {
        "form": form,
    }

    return render(request, "recipes/create_playlist.html", context)

@login_required
def playlist_list(request):
    user = request.user
    playlists = Playlist.objects.filter(created_by=user)
    context = {
        'playlist_list': playlists,
    }
    return render(request, 'recipes/playlist_list.html', context)

@login_required
def show_playlist(request, id):
    playlist = get_object_or_404(Playlist, id=id)
    context = {
        'playlist_object': playlist,
    }
    return render(request, 'recipes/playlist_detail.html', context)

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
