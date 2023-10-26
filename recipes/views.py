from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Playlist
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, PlaylistForm
from django.contrib.auth.models import User

@login_required
def delete_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    if request.method == "POST":
        playlist.delete()
        return redirect('playlist_list')

    context = {
        'playlist': playlist,
    }

    return render(request, 'recipes/delete_playlist.html', context)

@login_required
def edit_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect("show_playlist", id=playlist_id)
    else:
        form = PlaylistForm(instance=playlist)
        form.fields['recipes'].queryset = Recipe.objects.filter(created_by=request.user)

    context = {
        "playlist_object": playlist,
        "playlist_form": form
    }

    return render(request, "recipes/edit_playlist.html", context)

@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/delete.html', context)

@login_required
def edit_recipe(request, id):
    post = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=post)
    context = {
        "recipe_object": post,
        "recipe_form": form
    }

    return render(request, "recipes/edit.html", context)

@login_required
def show_playlist_recipes(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    recipes = playlist.recipes.filter(created_by=request.user)

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

@login_required
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
