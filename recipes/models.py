from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=250)
    picture = models.URLField()
    recipes = models.ManyToManyField(Recipe, related_name='playlists', blank=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.title
